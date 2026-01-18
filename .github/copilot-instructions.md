# AI Coding Agent Instructions for J2P

## Project Overview
**J2P** (likely "Jump to Python") is an educational Python learning project from a Korean programming textbook. It focuses on teaching object-oriented programming (OOP) concepts through progressive examples, primarily using **Chapter 5: Classes**.

### Architecture
- **Main Medium**: Jupyter Notebook (`j2p.ipynb`) for interactive teaching with markdown explanations and executable code cells
- **Supporting Examples**: `ch05/` contains three calculator implementations demonstrating OOP progression:
  - `calculator.py` - Function-based with global state (procedural approach)
  - `calculator2.py` - Multiple functions with separate global states (stateful functions)
  - `calculator3.py` - Class-based approach with instance state (OOP solution)

## Key Development Patterns

### 1. Progressive Example Structure
This project teaches OOP by showing the **evolution** from procedural → functional → object-oriented approaches:
- Each calculator file builds on lessons from the previous
- The notebook integrates theory (markdown) with practical examples (code cells)
- When adding new examples, follow this progression pattern

### 2. Class Design Pattern
Use simple, stateful classes similar to `Calculator` and `FourCal`:
```python
class Calculator:
    def __init__(self):
        self.result = 0  # Instance state
    
    def add(self, num):
        self.result += num
        return self.result
```
- Initialize state in `__init__`
- Methods modify and return instance state
- Single responsibility (one calculation focus per class)

### 3. Notebook Structure
Code cells alternate with markdown explanation cells:
- Markdown: Theory, problem explanation, design decisions
- Code cells: Class definition, usage example, test cases
- Keep cells focused (one concept per cell pair)
- Use execution count to verify cell order dependencies

## Critical Developer Workflows

### Running & Testing
- **Jupyter Notebook**: Execute cells sequentially in VS Code Jupyter extension
- **Direct Python Scripts**: From workspace root (with activated venv):
  ```bash
  source venv/bin/activate
  python j2p/ch05/calculator.py
  ```
- **Virtual Environment**: Python packages installed in `venv/` directory (required for reproducibility)

### When Adding New Content
1. Create example file in appropriate chapter directory (e.g., `ch05/`)
2. Define progression: problem → function approach → class solution
3. Add notebook cells explaining the "why" before showing code
4. Test in notebook before committing standalone files
5. Ensure variable names match between notebook and supporting files

## Project-Specific Conventions

### Naming & Structure
- **File naming**: Numbered suffixes for progression (e.g., `calculator.py`, `calculator2.py`, `calculator3.py`)
- **Class names**: Use descriptive names (`Calculator`, `FourCal` for 4-operation calculator)
- **Method names**: Simple, action-based (`add`, `sub`, `mul`, `div`)

### Error Handling
Current approach is minimal (e.g., FourCal checks division by zero). When expanding:
- Keep error handling simple and visible (educational, not production-ready)
- Return error messages rather than raising exceptions (simpler for learners)
- Document the "learner-friendly" tradeoff in comments

### Korean Content
Notebook contains Korean educational text. When modifying:
- Preserve Korean section headers and explanations
- Follow the existing markdown structure for consistency
- Comments in Python code can remain in English or match notebook language

## Known Integration Points

- **Notebook kernel**: Maintains state across cells; variables persist (e.g., `Cal1`, `a` instances)
- **Chapter organization**: Currently focused on Chapter 5 (Classes); future chapters likely to follow
- **Dependency**: None on external packages; all examples use Python stdlib only

## Quick Reference: Key Files
- [j2p/j2p.ipynb](../j2p/j2p.ipynb) - Main interactive notebook (Markdown + Code cells)
- [j2p/ch05/](../j2p/ch05/) - Standalone Python examples for Chapter 5
