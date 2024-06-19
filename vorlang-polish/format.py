import sys


class VorFormatter:
    def __init__(self, filename):
        self.filename = filename

    def format(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()

        # Remove all newlines
        lines = [line.strip() for line in lines if line.strip() != ""]

        formatted_lines = self.format_lines(lines)

        with open(self.filename, "w") as file:
            file.writelines(formatted_lines)

    def format_lines(self, lines):
        in_function = False
        last_import_index = self.get_last_import_index(lines)
        formatted_lines = []
        in_multiline_comment = False
        for i, line in enumerate(lines):
            if line.startswith("module"):
                formatted_lines.append(line + "\n")
                if i == last_import_index:
                    formatted_lines.append("\n")
            elif line.startswith("define"):
                in_function = True
                formatted_lines.append("\n" + line + "\n")
            elif line == "endfunc":
                in_function = False
                formatted_lines.append(line + "\n\n")
            elif "/*" in line and "*/" in line:
                formatted_lines.append("\n" + line.split("/*")[0])
                formatted_lines.append(
                    "/*" + line.split("/*")[1].split("*/")[0] + "*/\n"
                )
                formatted_lines.append(line.split("*/")[1] + "\n")
            elif line.strip().startswith("/*"):
                in_multiline_comment = True
                formatted_lines.append("\n" + line + "\n")
            elif line.strip().endswith("*/"):
                in_multiline_comment = False
                formatted_lines.append("\n" + line + "\n\n")
            elif in_multiline_comment:
                formatted_lines.append("\t" + line)
            elif line.strip().startswith("#"):
                formatted_lines.append("\n" + line + "\n")
            elif in_function:
                formatted_lines.append("\t" + line + "\n")
            else:
                formatted_lines.append(line + "\n")

        # Remove trailing newlines
        while formatted_lines and formatted_lines[-1] == "\n":
            formatted_lines.pop()

        return formatted_lines

    @staticmethod
    def get_last_import_index(lines):
        return max(i for i, line in enumerate(lines) if line.startswith("module"))


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Format a VOR file.")
    parser.add_argument("filename", help="The name of the file to format.")
    parser.add_argument(
        "-f", "--files", help="The names of the files to format.", nargs="+"
    )
    args = parser.parse_args()

    if args.files:
        for filename in args.files:
            if not filename.endswith(".vor"):
                print(
                    f"Invalid file extension for '{filename}'. Only .vor files are supported."
                )
                sys.exit(1)
            formatter = VorFormatter(filename)
            formatter.format()
    else:
        if args.filename:
            formatter = VorFormatter(args.filename)
            formatter.format()
        else:
            print("No filename provided.")
            sys.exit(1)

        if not args.filename.endswith(".vor"):
            print("Invalid file extension. Only .vor files are supported.")
            sys.exit(1)
