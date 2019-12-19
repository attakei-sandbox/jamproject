from docutils.nodes import NodeVisitor
from docutils.writers import Writer as BaseWriter


class ReportTranslator(NodeVisitor):
    def __init__(self, document):
        super().__init__(document)
        self.body = []

    def visit_any(self, node):
        if "report" not in node:
            return
        report = node["report"]
        if not report.has_message():
            return
        self.body.append([
            f"{node.source}:{node.line}-",
            [m.body for m in report.messages],
        ])

    def pass_node(self, node):
        pass

    def __getattr__(self, name):
        if name.startswith("visit_"):
            return self.visit_any
        if name.startswith("depart_"):
            return self.pass_node
        return super().__getattr__(name)

class Writer(BaseWriter):
    def translate(self):
        translator = ReportTranslator(self.document)
        self.document.walkabout(translator)
        self.output = ""
        for t in translator.body:
            self.output += f"{t[0]}\n1"
            self.output += "\n".join([f"\t{m}" for m in t[1]])
            self.output += "\n"
