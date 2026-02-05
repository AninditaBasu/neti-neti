from phonological_probe_demo import probe_string

def main():
    word = input("Please enter a string: ").strip()
    results = probe_string(word)

    print("\n=== Probe results ===")
    print(results)

if __name__ == "__main__":
    main()

