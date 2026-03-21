"""
In this file, the implementation of writing a section is handled.

Each section is a function. This file will be used in conjunction
with the yaml file parsing to generate the main documantation html code.
"""

from .utils import InitError, indent, escape


def get_params_from_list(param_list: list[dict]):
    return [Parameter(p) for p in param_list]


def get_returns_from_list(param_list: list[dict]):
    return [Returns(r) for r in param_list]


def get_examples(examples_list):
    for n, i in enumerate(examples_list):
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
        self.full_name: str = full_name

        try:
            data = function_data[full_name]
            self.short_name: str = data["short_name"]
            self.description: str = data["description"]
            self.syntax: list[str] = [escape(d) for d in data["syntax"]]
            self.params: list[Parameter] = get_params_from_list(data["params"])
            self.returns: list[Returns] = get_returns_from_list(data["returns"])
            self.time_comp: str = data["time_comp"]
            self.examples: list[str | Code] = get_examples(data["examples"])
            self.init_complete = True
            Section.count += 1
        except:
            self.init_complete = False
            print(f"Warning: Skipped {self.full_name}")
            raise InitError("Unable to initialize section.")


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
            if isinstance(e, Code):
                out += f'    <pre><code class="language-cpp">{e.code}</code></pre>\n'
            else:
                out += f"    <p>{e}" + "</p>" + "\n"
        return out


    def get_returns_section(self):
        out = '<h3>Returns</h3>\n<div class="params-section">\n'

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



# Testing 
if __name__ == "__main__":
    import yaml
    with open(r"CodeGen\functions.yaml", "r") as file:
        html_data: dict = yaml.safe_load(file)
    
    print(html_data.keys())
