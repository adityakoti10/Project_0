# Compact Finance Tracker (Version 1)

txs = []

def add_tx(typ, amt, cat, desc):
    txs.append({"typ": typ, "amt": amt, "cat": cat, "desc": desc})

def get_bal():
    return sum(t["amt"] if t["typ"] == "inc" else -t["amt"] for t in txs)

def show_txs():
    print("\n--- History ---")
    if not txs:
        print("No transactions.")
        return
    for t in txs:
        print(f"{t['typ'].upper():<3} | ₹{t['amt']:<8} | {t['cat']:<10} | {t['desc']}")

def main():
    while True:
        print("\n1.Inc  2.Exp  3.History  4.Bal  5.Exit")
        ch = input("> ")
        
        if ch in ("1", "2"):
            typ = "inc" if ch == "1" else "exp"
            try:
                amt = float(input("Amount: ₹"))
                cat = input("Category: ")
                desc = input("Description: ")
                add_tx(typ, amt, cat, desc)
                print("Added!")
            except ValueError:
                print("Invalid amount!")
        elif ch == "3":
            show_txs()
        elif ch == "4":
            print(f"Balance: ₹{get_bal():,.2f}")
        elif ch == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

