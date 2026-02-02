# Command-line interface for phonological plausibility demo

from phonological_plausibility_demo import analyse_string

def main():
    word = input("Please enter a string: ")
    results = analyse_string(word)

    print(f"\nInput string: {results['input']}")
    print(f"Generated skeletons: {results['skeletons']}")

    for entry in results["evaluations"]:
        print(f"\n{entry['family']}")
        print(f"  Strain index: {entry['strain']}")
        print(f"  Plausibility score (1–5): {entry['plausibility']}")
        if entry["diagnostics"]:
            print("  Diagnostics:")
            for d in entry["diagnostics"]:
                print(f"   - {d}")
        else:
            print("  Diagnostics: none")

if __name__ == "__main__":
    main()
