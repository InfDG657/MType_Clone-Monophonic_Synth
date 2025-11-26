# Python Coding Assistant Preferences

## Core Principle
Provide ONLY what is requested. Do not refactor existing code. Do not add dependencies or helper functions unless explicitly asked. All additions must be self-contained.

## My Coding Style

### Readability Requirements
- Keep logic traceable and readable
- Avoid excessive function nesting or chaining
- If a function calls another function calls another function, you've gone too far
- When helper functions are necessary, keep them adjacent to related code
- Prefer inline logic when reasonably possible

### Anti-Patterns to AVOID
- ❌ Global variables
- ❌ Callback hell / deeply nested functions  
- ❌ Function chaining where I have to reference 5 other functions to understand what's happening
- ❌ Over-abstraction that hides simple logic
- ❌ "Clever" one-liners that sacrifice readability

### Code Organization
- Single script files are my primary format
- Functions should be self-explanatory from their name


## Libraries I Use Regularly

### GUI Development
- **Tkinter** - My primary GUI library
  - ALWAYS use `.grid()` layout method
  - When I request GUI elements, provide ONLY the structure I specify
  - DO NOT fill in command parameters unless I explicitly ask
  - DO NOT assume what buttons/widgets should do
  - Example: If I say "two buttons, a slider, and a text box" - give me exactly that in a grid layout with NO functionality assumptions

### Data Processing
- **Pandas** 
- **NumPy** 

### Pattern Matching
- **Regex** - I frequently need regex patterns but don't want to figure them out manually
  - Provide patterns with explanation of what each part does
  - Include example test cases when relevant

### Future Libraries (Not Yet Using)
- Transformers
- TensorFlow
- PyTorch

## How to Help Me

### Response Format
1. Generate the code I requested (self-contained)
2. Explain what it does in 1-2 sentences
3. Ask if I'm satisfied
4. If not satisfied, ask clarifying questions to improve

### Level of Explanation
- **Simple tasks** (syntax I forgot, basic methods): Minimal explanation
- **Complex logic** (regex patterns, tricky algorithms): Explain what it does
- **Confusing lines**: I'll ask follow-up questions if I don't understand something

### Error Debugging
When I paste an error:
- Explain WHY the error happened
- Provide the fix
- Show the corrected code

## What NOT to Do

### CRITICAL: Scope Boundaries
- ❌ DO NOT refactor code I didn't ask you to change
- ❌ DO NOT add attributes to existing classes unless requested
- ❌ DO NOT create helper functions unless I specifically ask for them
- ❌ DO NOT modify my existing methods when adding new ones
- ❌ DO NOT make assumptions about functionality

### Example of What I DON'T Want:
```
Me: "Add a method to validate email addresses"

Bad Response:
- Adds the validation method
- Also adds self.validated_emails attribute
- Also adds self.invalid_emails attribute  
- Also creates 3 helper functions
- Also refactors my __init__ method
- Now I don't recognize my own code

Good Response:
- Just the validation method, self-contained
- Uses only what already exists in the class
- Clear and simple
```

## Code Examples of My Style



Example 1: How I like my tkinter classes
'''widgets defined in one method, widgets placed in the second. bindings after placements and widgets. Note that although place is used here, this is to make the click and place method functionality work. It is not to place buttons. I will specify when place or pack needs to be used. otherwise default to grid like instructed.'''
class AlignmentWin(tk.Toplevel):
    def __init__(self, workspace):
        super().__init__()
        self.workspace = workspace
        self.geometry(f'470x55+0+642')
        self.widgetlist =  []

        self.widgets()
        self.placement()

        self.bind('<KeyPress-a>', self.workspace.handle_keypress)
        self.bind('<KeyPress-s>', self.workspace.handle_keypress)
        self.bind('<KeyPress-d>', self.workspace.handle_keypress)
        self.bind('<KeyPress-w>', self.workspace.handle_keypress)
        
    def widgets(self):
        self.btn1 = ttk.Button(self, text="Align Top", command=self.align_top)
        self.btn2 = ttk.Button(self, text="Align Btm", command=self.align_bottom)
        self.btn3 = ttk.Button(self, text="Align Left", command=self.align_left)
        self.btn4 = ttk.Button(self, text="Align Right", command=self.align_right)

    def placement(self):
         self.rowconfigure(0, weight=1)
         self.columnconfigure((0,1,2,3), weight=1, uniform='a')

         self.btn1.grid(row=0, column=0, sticky='nesw', padx=5,pady=10)
         self.btn2.grid(row=0, column=1, sticky='nesw', padx=5,pady=10)
         self.btn3.grid(row=0, column=2, sticky='nesw', padx=5,pady=10)
         self.btn4.grid(row=0, column=3, sticky='nesw', padx=5,pady=10)

    def get_anchors(self):
        self.widgetlist = [w for w in self.workspace.winfo_children() if w != self.workspace.referencewidget]
        self.adjustwidget = self.widgetlist.pop()
        self.widgetbottoms = [float(w.place_info().get('rely')) + (w.winfo_height() / 2)/self.workspace.height for w in self.widgetlist]
        

    def align_top(self):
        self.get_anchors()
        adjusty = float(self.adjustwidget.place_info().get('rely'))
        self.widgetlist = list(zip(self.widgetlist, self.widgetbottoms))
        self.widgetlist = sorted(self.widgetlist, key = lambda y: abs(y[1] - adjusty))
        #for w in self.widgetlist:
             
        new_x = float(self.widgetlist[0][0].place_info().get('relx'))
        self.adjustwidget.place(relx = new_x, rely= adjusty, anchor='w')
        
    def align_bottom(self):
        self.widgetlist = [w for w in self.workspace.winfo_children() if w != self.workspace.referencewidget]
        self.adjustwidget = self.widgetlist.pop()
        adjusty = float(self.adjustwidget.place_info().get('rely'))
        self.widgetlist = sorted(self.widgetlist, key = lambda y: adjusty - float(y.place_info().get('rely')))
        new_x = float(self.widgetlist[0].place_info().get('relx'))
        self.adjustwidget.place(relx = new_x, rely= adjusty, anchor='w')

    def align_left(self):
        self.widgetlist = [w for w in self.workspace.winfo_children() if w != self.workspace.referencewidget]
        self.adjustwidget = self.widgetlist.pop()
        adjustx = float(self.adjustwidget.place_info().get('relx'))
        self.widgetlist = sorted(self.widgetlist, key = lambda y: float(y.place_info().get('relx')) - adjustx)
        new_y = float(self.widgetlist[0].place_info().get('rely'))
        self.adjustwidget.place(relx = adjustx, rely= new_y, anchor='w')

    def align_right(self):
        pass

Example 2: How I typically use helper functions and classes as well as list comprehension, loops etc. Basically my preferred style
'''For completeness I showed the one function with a bunch of nested functions. I don't typically want this if it can be avoided.'''  
def find_all_emails(text):
    pattern1 = r'(?:^|[\s\n]|(?<=[^A-Za-z0-9._%-]))[A-Za-z0-9][A-Za-z0-9._%-]{0,28}[A-Za-z0-9]@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    pattern2 = r'[A-Za-z0-9][A-Za-z0-9._%-]{0,28}[A-Za-z0-9]@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    matches_pattern1 = re.findall(pattern1, text)
    matches_pattern1 = [match.strip() for match in matches_pattern1]
    matches_pattern2 = re.findall(pattern2, text)
    all_matches = list(matches_pattern1)
    for match in matches_pattern2:
        if match not in all_matches:
            all_matches.append(match)
    return all_matches

class Redactor():
    def __init__(self, first_name, last_name, extracted_data_path='extracted_text_output.txt'):
        self.extracted_data = self.load_extracted_data(extracted_data_path)
        self.first_name = first_name
        self.last_name = last_name
        self.redacted = []
        self.redact_dictionary = {}
        
        # Pass 1: Find and redact (before cleaning)
        self.find_redact_items()
        self.perform_redact()
        
        # Clean text (Redacted tokens stay protected)
        self.extracted_data = self.clean_text()
        
        # Pass 2: Find and redact again (after cleaning)
        self.find_redact_items()
        self.perform_redact()
            
    def load_extracted_data(self, data_path):
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Extracted data file not found: {data_path}")
            return None

    def find_redact_items(self):
        phone_patterns = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', self.extracted_data)
        birthdates = re.findall(r'(?:(?:\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[/\w]*\s+\d{2,4}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}\s+\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{2,4}|\d{2,4}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}|\d{1,4}[/-]\d{1,4}(?:[/-]\d{2,4})?).{0,50}?birth|birth.{0,50}?(?:\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[/\w]*\s+\d{2,4}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}\s+\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{2,4}|\d{2,4}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}|\d{1,4}[/-]\d{1,4}(?:[/-]\d{2,4})?))', self.extracted_data, re.IGNORECASE | re.DOTALL)
        emails = find_all_emails(self.extracted_data)
        social_security = re.findall(r'\b\d{3}-?\d{2}-?\d{4}\b', self.extracted_data)
        id_numbers = re.findall(r'(?i)\bid(?:[-_\s]*(?:number|num|no|#))?\s*[:=#-]?\s*(\d{1,20})', self.extracted_data)
        patterns_for_redaction = phone_patterns + birthdates + social_security + emails + id_numbers + [self.first_name, self.last_name]
        for i in patterns_for_redaction:
            if i and i in self.extracted_data and i not in self.redacted:
                self.redacted.append(i)
                
    def perform_redact(self):
        
        new_items = [item for item in self.redacted if item not in self.redact_dictionary]
    
        start_index = len(self.redact_dictionary)
        
        for i, item in enumerate(new_items, start=start_index):
            self.redact_dictionary[item] = f'_Redacted{i}_'

        redacted_file = self.extracted_data
    
        for k, v in self.redact_dictionary.items():
            redacted_file = re.sub(re.escape(k), v, redacted_file, flags=re.IGNORECASE)

        self.extracted_data = redacted_file

    def clean_text(self):
        text = self.remove_weird_unicode(self.extracted_data)
        text = self.collapse_spaced_letters(text)
        text = self.add_camelcase_boundaries(text)
        text = self.add_number_boundaries(text)
        text = self.segment_smooshed_text(text)
        text = self.remove_junk_lines(text)
        return text
    
    def remove_weird_unicode(self, text):
        """Keep only printable ASCII characters"""
        allowed_chars = string.ascii_letters + string.digits + string.punctuation + ' \n\t'
        cleaned = ''.join(char if char in allowed_chars else ' ' for char in text)
        return cleaned
    
    def collapse_spaced_letters(self, text):
        """Fix 'T E X T' → 'TEXT'"""
        pattern = r'\b([A-Za-z])\s+(?=[A-Za-z]\s)'
        def collapse_match(match):
            return match.group(1)
        while re.search(pattern, text):
            text = re.sub(pattern, collapse_match, text)
        text = re.sub(r'\b([A-Za-z])\s+([A-Za-z])\b', r'\1\2', text)
        return text
    
    def add_camelcase_boundaries(self, text):
        """Add spaces to CamelCase: 'SickamoreStreet' → 'Sickаmore Street'"""
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
        return text
    
    def add_number_boundaries(self, text):
        parts = re.split(r'(_Redacted\d+_)', text)
        processed_parts = []
        for part in parts:
            if re.match(r'_Redacted\d+_', part):
                # Don't process _Redacted#_ tokens
                processed_parts.append(part)
            else:
                # Process normally
                part = re.sub(r'(\d)([A-Za-z])', r'\1 \2', part)
                part = re.sub(r'([A-Za-z])(\d)', r'\1 \2', part)
                processed_parts.append(part)
        
        return ''.join(processed_parts)
    
    def segment_smooshed_text(self, text):
        lines = text.split('\n')
        segmented_lines = []
        for line in lines:
            words = line.split()
            segmented_words = []
            for word in words:
                # Skip _Redacted#_ tokens
                if re.match(r'_Redacted\d+_', word):
                    segmented_words.append(word)
                    continue
                
                # Skip segmentation for emails, URLs
                if '@' in word or '.com' in word or '.org' in word or '.edu' in word or '.net' in word:
                    segmented_words.append(word)
                    continue
                
                # Split word into alphabetic and non-alphabetic chunks
                chunks = re.findall(r'[A-Za-z]+|[^A-Za-z]+', word)
                segmented_chunks = []
                for chunk in chunks:
                    # Skip all-caps chunks (likely acronyms/abbreviations)
                    if chunk.isupper() and len(chunk) > 1:
                        segmented_chunks.append(chunk)
                    elif chunk.isalpha():
                        segments = wordninja.split(chunk)
                        segmented_chunks.extend(segments)
                    else:
                        segmented_chunks.append(chunk)
                segmented_words.append(' '.join(segmented_chunks))
            segmented_lines.append(' '.join(segmented_words))
        return '\n'.join(segmented_lines)
    
    def remove_junk_lines(self, text):
        """Remove lines with <20% alphanumeric or repeated characters"""
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            if not line.strip():
                cleaned_lines.append(line)
                continue
            total_chars = len(line.strip())
            if total_chars == 0:
                continue
            alphanumeric_count = sum(1 for char in line if char.isalnum())
            alphanumeric_ratio = alphanumeric_count / total_chars
            if alphanumeric_ratio < 0.20:
                continue
            if re.search(r'(.)\1{5,}', line):
                continue
            cleaned_lines.append(line)
        return '\n'.join(cleaned_lines)