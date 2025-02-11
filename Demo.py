import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class TogaApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=ROW))

        # Tabelle erstellen
        table = toga.Table(
            headings=["Hello", "World"],
            data=[
                ("root1", "value1"),
                ("root2", "value2"),
                ("root3", "value3"),
                ("root4", "value4"),
            ],
        )

        # Rechte Box mit Buttons
        button_box = toga.Box(style=Pack(direction=COLUMN))
        for i in range(6):
            button = toga.Button(
                f"Hello world {i}",
                style=Pack(padding=5)
            )
            button_box.add(button)

        # Beide Elemente ins Haupt-Layout
        main_box.add(table)
        main_box.add(button_box)

        self.main_window = toga.MainWindow(title="Toga Demo")
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return TogaApp("Toga Demo", "org.beeware.toga.demo")

if __name__ == "__main__":
    main().main_loop()

