from __future__ import annotations

import yaml
import html


def indent(string: str, no_indents = 1, indent_spaces = 4):
    """Indents an entie block of text by a fixed amount.

    Parameters
    ----------
    string : str
        The text to indent.
    time : int
        The number of times the text should be indented.
    indent_spaces : int
        The number of spaces (" ") each indent consists of.
    """
    spaces = ' ' * no_indents * indent_spaces
    return '\n'.join([spaces + i for i in string.split('\n')])


def escape(x): return html.escape(x, quote=False)


def get_params_from_list(param_list: list[dict]):
    return [Parameter(p) for p in param_list]


def get_returns_from_list(param_list: list[dict]):
    return [Returns(r) for r in param_list]


def get_examples(examples_list):
    for n,i in enumerate(examples_list):
        if str(i).endswith(".cpp"):
            examples_list[n] = Code(i)
    return examples_list



class Code:
    def __init__(self, filename):
        filepath = r"CodeGen\\Examples\\" + filename
        with open(filepath, "r") as file:
            file_content = file.read()

        self.code = escape(file_content)

    def __str__(self):
        return self.code


class Parameter:
    def __init__(self, param_details: dict):
        self.name = list(param_details.keys())[0]
        self.type, self.description = param_details[self.name]
        self.name = escape(self.name)

    def __str__(self):
        return f"{self.name} : {self.type}\n\t{self.description}"


class Returns:
    def __init__(self, param_details: dict):
        self.name = list(param_details.keys())[0]
        self.description = param_details[self.name][0]
        self.name = escape(self.name)

    def __str__(self):
        return f"{self.name}\n\t{self.description}"


class Section:
    count = 0

    def __init__(
        self,
        full_name: str,
        function_data: dict
    ):
       data = function_data[full_name]
       Section.count += 1
       
       self.full_name = full_name
       self.short_name = data["short_name"]
       self.description = data["description"]
       self.syntax = [escape(d) for d in data["syntax"]]
       self.params: list[Parameter] = get_params_from_list(data["params"])
       self.returns: list[Returns] = get_returns_from_list(data["returns"])
       self.time_comp = data["time_comp"]
       self.examples = get_examples(data["examples"])


    def get_syntax_section(self):
        out = "<h3>Syntax</h3>\n"
        for s in self.syntax:
            out += f'    <pre><code class="language-cpp">{s}</code></pre>\n'
        return out


    def get_params_section(self):
        out = '<h3>Parameters</h3>\n<div class="params-section">\n'
        for p in self.params:
            out += f"""\
    <div class="param-item">
        <div class="param-name">{p.name} : <span class="param-type">{p.type}</span></div>
        <div class="param-description">{p.description}</div>
    </div>\n"""
            
        out += "</div>"
        return out
    

    def get_examples_section(self):
        out = "<h3>Examples</h3>\n"
        for e in self.examples:
            if(isinstance(e, Code)):
                out += f'    <pre><code class="language-cpp">{e.code}</code></pre>\n'
            else:
                out += f"    <p>{e}" + "</p>" + "\n"
        return out


    def get_returns_section(self):
        out ='<h3>Returns</h3>\n<div class="params-section">\n'

        for r in self.returns:
            out += f"""<div class="param-item">
        <div class="param-name">{r.name}</div>
        <div class="param-description">{r.description}</div>
    </div>"""
        out += "\n</div>"
        return out


    def write_section(self):
        return f"""<!-- {self.short_name}() Section -->
<section class="content-section{" active" if (Section.count == 1) else ""}" id="{self.short_name}">
    <h2>{self.full_name}</h2>
    <p>{self.description}</p>

    {self.get_syntax_section()}

{indent(self.get_params_section())}

{indent(self.get_returns_section())}

    <h3>Time Complexity</h3>
    <p style="font-weight: bold; font-size: 1.15rem;">O(n)</p>

    {self.get_examples_section()}
</section>\n\n\n"""


if __name__ == "__main__":
    with open(r'CodeGen\functions.yaml', 'r') as file:
        html_data = yaml.safe_load(file)

    html_file = ""

    for func in html_data:
        sec = Section(func, html_data)
        html_file += sec.write_section()
    
    print(html_file)

    with open("test.html", 'w') as outFile:
        outFile.write(html_file)

    # data = html_data["numxx::zeros<T>"]
    # print(get_params_from_list(data["params"]))
    # print(data["returns"])
