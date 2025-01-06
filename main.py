import sys
import config
import combine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise "invalid arguments"
    config_path = sys.argv[1]
    config = config.Config(config_path)
    combiner = combine.Combiner(config)
    combiner.combine()
