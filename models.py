from dataclasses import dataclass, field


@dataclass
class Combo:
    source_file: str
    name: str
    slots: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class ComboVersion:
    combo_id: str
    combo_versions: dict[str, Combo] = field(default_factory=dict)

    def add_version(self, combo: Combo) -> None:
        self.combo_versions[combo.source_file] = combo


@dataclass
class Menu:
    combos: dict[str, ComboVersion] = field(default_factory=dict)

    def add_combo(self, json_data: dict) -> None:
        source = json_data['source']

        for item in json_data['combos']:
            combo_id = item['combo_id']

            combo = Combo(
                source_file=source,
                name=item['name'],
                slots=item['slots'],
            )

            if combo_id not in self.combos:
                self.combos[combo_id] = ComboVersion(combo_id)

            self.combos[combo_id].add_version(combo)
