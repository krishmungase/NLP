```markdown
# 🐍 Python Virtual Environment Setup

This guide shows how to **create** and **activate** a Python virtual environment.

---

## 📌 Why use virtual environment?

- Keeps project dependencies isolated  
- Avoids version conflicts  
- Clean & professional setup  

---

## 🔹 Step 1: Create virtual environment

### Mac / Linux
```bash
python3 -m venv venv
```

### Windows
```bash
python -m venv venv
```

---

## 🔹 Step 2: Activate environment

### Mac / Linux
```bash
source venv/bin/activate
```

### Windows
```bash
venv\Scripts\activate
```

After activation, you'll see:
```
(venv)
```

---

## 🔹 Step 3: Install packages

```bash
pip install package_name
```

Example:
```bash
pip install boto3
```

---

## 🔹 Step 4: Deactivate environment

```bash
deactivate
```

---

## 💡 Always activate before running

### Mac / Linux
```bash
source venv/bin/activate
```

### Windows
```bash
venv\Scripts\activate
```
```