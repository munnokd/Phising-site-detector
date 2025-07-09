import pyshark
import os
import pandas as pd

def extract_features(pcap_file):
    try:
        cap = pyshark.FileCapture(pcap_file, only_summaries=True)
        packets = list(cap)
        lengths = [int(p.length) for p in packets if hasattr(p, 'length')]
        tcp_count = sum(1 for p in packets if 'TCP' in p.info)
        udp_count = sum(1 for p in packets if 'UDP' in p.info)

        features = {
            "packet_count": len(packets),
            "avg_packet_size": sum(lengths) / len(lengths) if lengths else 0,
            "total_bytes": sum(lengths),
            "tcp_packet_count": tcp_count,
            "udp_packet_count": udp_count
        }
        cap.close()
        return features
    except Exception as e:
        print(f"Error processing {pcap_file}: {e}")
        return None

def batch_extract():
    rows = []
    for file in os.listdir("captures"):
        if file.endswith(".pcap"):
            label = 1 if file.startswith("1_") else 0
            features = extract_features(os.path.join("captures", file))
            if features:
                features['label'] = label
                rows.append(features)

    df = pd.DataFrame(rows)
    df.to_csv("network_features.csv", index=False)
    print("Extracted features saved to network_features.csv")

if __name__ == "__main__":
    batch_extract()

