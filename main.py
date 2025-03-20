import argparse
from train import train

def main():
    parser = argparse.ArgumentParser(description="ATDP Walker")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    train_parser = subparsers.add_parser('train', help="Train the model")
    train_parser.add_argument('--job-id', type=str, required=True, help="Job ID for tracking this training run")

    args = parser.parse_args()
    
    if args.command == "train":
        train()

if __name__ == "__main__":
    main()
