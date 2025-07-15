# Elevate Labs Task 6: Password Strength Evaluation

## Objective

This task focuses on understanding what makes a password secure. It includes generating passwords of varying strengths using a Python script and evaluating them using online password strength tools.

---

## Tools Used

- Python 3
- PasswordMonster (https://passwordmonster.com)

---

## Password Generator Script

The following Python script was used to generate passwords with customizable strength levels by controlling:
- Length
- Character types: Uppercase, Lowercase, Digits, Symbols
![image](https://github.com/user-attachments/assets/fa8c297e-84db-4a61-96a5-d2c90b474c6b)

![image](https://github.com/user-attachments/assets/4ff78b4c-8141-421b-9f43-91be607b6cd5)

---

## Password Evaluation Results

### 1. Weak Password: `Password123`

- Length: 11
- Contains: Uppercase, Lowercase, Numbers
- No symbols
- Verdict: **Very Weak**
- Time to crack: 0 seconds

<img width="1408" height="716" alt="image" src="https://github.com/user-attachments/assets/265baa5f-faca-4485-9790-310bd3b6b1aa" />

---

### 2. Weak Password: `iloveindia`

- Length: 10
- Contains: Lowercase only
- Verdict: **Very Weak**
- Time to crack: 4.29 seconds

<img width="1373" height="655" alt="image" src="https://github.com/user-attachments/assets/874fb5d7-5277-495d-9b73-23bbb7681175" />


---

### 3. Strong Password: `SDNETTRH`

- Length: 8
- Contains: Uppercase only
- Verdict: **Strong**
- Time to crack: 11 months

![image](https://github.com/user-attachments/assets/6b4aef13-1be3-422b-9a6b-b0141766ae40)

---

### 4. Very Strong Password: `MIRSe3ur@dfi$sworle`

- Length: 19
- Contains: Uppercase, Lowercase, Digits, Symbols
- Verdict: **Very Strong**
- Time to crack: 3 hundred trillion years

<img width="1196" height="536" alt="image" src="https://github.com/user-attachments/assets/53ec9dd9-70e6-4d4a-9bfa-7d83b817c7ec" />


---

## Key Takeaways

- Passwords with dictionary words or common patterns are cracked instantly.
- The inclusion of all character types significantly increases password strength.
- Longer passwords increase resistance against brute-force and dictionary attacks.

---

## Common Attack Types

| Attack Type         | Description                                                                |
|---------------------|----------------------------------------------------------------------------|
| Brute Force         | Attempts every possible combination until the correct one is found         |
| Dictionary Attack   | Tries commonly used words and leaked passwords from public datasets        |
| Credential Stuffing | Tests stolen username/password combinations on multiple services           |

---

## Best Practices

- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, and symbols
- Avoid dictionary words, names, or patterns
- Use a password manager
- Enable multi-factor authentication (MFA)

---

