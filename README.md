# Prime Number Checker

This is a simple Python script that takes a list of numbers from user input, detects prime numbers, and prints which ones are prime.

## 🔧 Features

- Accepts input in various formats: numbers separated by **spaces, commas, or dots**
- Automatically filters non-integer input and handles errors
- Efficient prime number detection using square root optimization

## 📥 Input Format

When prompted, enter numbers like:

```
4, 7, 10, 13.17 18
```

Any combination of commas, dots, or spaces will be parsed correctly.

## ✅ Example Output

```
write numbers: 3, 4, 5
3 is prime
4 is not prime
5 is prime
Prime numbers: [3, 5]
```

## 💡 How it works

- The input string is cleaned using `replace(',', ' ').replace('.', ' ')`.
- The cleaned string is split and converted into integers using list comprehension.
- Each number is checked for primality by trying to divide it by all integers from `2` up to the square root of the number.
- Results are printed and prime numbers are stored in a list.

## 🧠 Requirements

- Python 3.x

## 🚀 Running the Script

```bash
python ukol2.py
```

## 📁 File Structure

```
ukol2.py        # Main script
README.md       # This file
```

## 🤝 License

MIT License – free to use and modify.
