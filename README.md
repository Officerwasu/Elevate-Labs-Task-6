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


---

## Password Evaluation Results

### 1. Weak Password: `Password123`

- Length: 11
- Contains: Uppercase, Lowercase, Numbers
- No symbols
- Verdict: **Very Weak**
- Time to crack: 0 seconds

![Password123 Result](https://private-user-images.githubusercontent.com/64682548/460969948-202fc6e8-ee7d-49a5-8c55-746674687763.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEzNjIzMzAsIm5iZiI6MTc1MTM2MjAzMCwicGF0aCI6Ii82NDY4MjU0OC80NjA5Njk5NDgtMjAyZmM2ZTgtZWU3ZC00OWE1LThjNTUtNzQ2Njc0Njg3NzYzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzAxVDA5MjcxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNhZDMwZjMzODI0YjBlOWY3MzhmZTgzMzE3Y2FhMDkzZmZjYzU0NDdmMGQ0ZGI1NGFmODBmOWI5ZDkwM2RiNTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.kwtwOTakdS7KG701cRTPluGbD2y0wotnI8z7vyzyiFI)

---

### 2. Weak Password: `iloveindia`

- Length: 10
- Contains: Lowercase only
- Verdict: **Very Weak**
- Time to crack: 4.29 seconds

![iloveindia Result](https://private-user-images.githubusercontent.com/64682548/460970829-712bb65d-e30f-4f70-ad91-0408ed112046.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEzNjIzMzAsIm5iZiI6MTc1MTM2MjAzMCwicGF0aCI6Ii82NDY4MjU0OC80NjA5NzA4MjktNzEyYmI2NWQtZTMwZi00ZjcwLWFkOTEtMDQwOGVkMTEyMDQ2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzAxVDA5MjcxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhZTMwMDhjYjIwYzg0ODQ0Y2VkNTZhMjk1YTRjOTliNzQ2ZDIzNjVkNjE3ODFjOGI2ZDU3ZDE2NmY0YTU3MjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.fp2hfQ1TdeJZIfac4nZp7KAeUJxW7eUm8AfKF-X2Y-8)

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

![Very Strong Password Result](https://private-user-images.githubusercontent.com/64682548/460972111-dc961ff4-1618-4107-9c99-ab92b4947219.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTEzNjIzMzAsIm5iZiI6MTc1MTM2MjAzMCwicGF0aCI6Ii82NDY4MjU0OC80NjA5NzIxMTEtZGM5NjFmZjQtMTYxOC00MTA3LTljOTktYWI5MmI0OTQ3MjE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzAxVDA5MjcxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTlkNmY1MGJlYTJkYTY0NGYwNGU1OTU3ZGNlZTIyYThiYzZlMDFmYjliOWE3ZGNiOWNmNTU0ZTNhMTdiM2ExNmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.66fMup4TzVyZI_wM9k8QSTxdNiTO1-6YABKq6NTc4Pg)

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

## Repository Structure

