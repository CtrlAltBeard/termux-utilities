# Contributing to Termux Utilities

We welcome contributions! Here’s how you can help:

---

## **📌 How to Contribute**

### **1. Report Bugs**

- Open an issue on GitHub with:
  - A **clear title** describing the issue.
  - **Steps to reproduce** the bug.
  - **Expected vs. actual behavior**.
  - **Screenshots/logs** (if applicable).

### **2. Suggest Features**

- Open an issue with:
  - A **detailed description** of your idea.
  - **Use cases** (how it would help you/others).

### **3. Submit Pull Requests**

1. **Fork** the repo.
2. **Create a feature branch**: `git checkout -b feature/your-feature`.
3. **Commit your changes**: `git commit -m "Add your feature"`.
4. **Push to the branch**: `git push origin feature/your-feature`.
5. **Open a Pull Request** on GitHub.

---

## **🎯 Guidelines**

### **Code Style**

- **Bash scripts**: Follow [ShellCheck](https://www.shellcheck.net/) recommendations.
- **Python scripts**: Follow [PEP 8](https://pep8.org/) guidelines.
- **Indentation**: Use **4 spaces** (no tabs).
- **Comments**: Add **clear, concise comments** for complex logic.

### **Testing**

- **Test your changes** before submitting.
- **Verify on Termux**: Ensure scripts work on a **real device** (not just a VM).
- **Edge cases**: Test with unusual inputs (e.g., empty files, missing directories).

### **Documentation**

- Update **READMEs** if your change affects usage.
- Add **comments** to explain non-obvious logic.
- Use **consistent naming** (e.g., `snake_case` for variables).

---

## **📂 Adding New Scripts**

1. **Place in the correct folder** (`system/`, `battery/`, `storage/`, or `weather/`).
2. **Add to the folder’s `README.md`**:
  - Brief description.
  - Usage example.
  - Customization tips (if any).
3. **Ensure it’s anonymized**:
  - No hardcoded paths (use `$HOME`).
  - No personal info (e.g., nicknames, emails).
4. **Make it executable**: `chmod +x script.sh`.

---

## **🤝 Code of Conduct**

- Be **respectful** and **inclusive**.
- **No personal attacks** or harassment.
- **Constructive feedback** only.

---

## **📜 License**

By contributing, you agree your submissions are licensed under the **MIT License**.
