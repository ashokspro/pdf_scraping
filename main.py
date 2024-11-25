import pdfplumber


def extract_and_format_names(pdf_path, subject_code):
    names = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split("\n")
            for i, line in enumerate(lines):
                # Check if the line contains the subject code
                if subject_code in line:
                    # Traverse upwards to find the name of the candidate
                    for j in range(i - 1, -1, -1):
                        if "NameoftheCandidate" in lines[j]:
                            name = lines[j].split("NameoftheCandidate")[-1].strip()
                            names.append(name.upper())  # Convert to uppercase
                            break
    return names


def format_names_for_output(names):
    formatted_names = "\n".join(names)
    return formatted_names


def display_output(subject_code, names):
    formatted_names = format_names_for_output(names)
    total_students = len(names)
    result = f"{subject_code.upper()}\n\n{formatted_names}\n\nTotal number of students: {total_students}"
    return result


# Example usage
pdf_file = "C:/Users/ashok/Downloads/114_05.pdf"
subject_count = int(input("ENTER TOTAL SUBJECT COUNT: "))

for i in range(subject_count):
    subject_code = input("ENTER SUBJECT CODE: ")
    subject_name = input("ENTER SUBJECT NAME: ")
    names = extract_and_format_names(pdf_file, subject_code)
    names = [entry.split(' DATEOFBIRTH ')[0] for entry in names]
    names = [name[:-1] + " " + name[-1] for name in names]
    output = display_output(subject_name, names)

    print(f"\n{output}")
