from dataclasses import dataclass
from typing import Optional, List

DIRECTION_SYNONYMS = {
    "n": "north", "north": "north",
    "e": "east", "east": "east",
    "s": "south", "south": "south",
    "w": "west", "west": "west",
}

VERB_SYNONYMS = {
    "go": "go", "move": "go",
    "look": "look", "inspect": "look",
    "take": "take", "get": "take",
    "drop": "drop",
    "use": "use",
    "unlock": "unlock",
    "inventory": "inventory", "inv": "inventory",
    "quit": "quit", "exit": "quit"
}

@dataclass
class Command:
    verb: str
    obj: Optional[str] = None
    target: Optional[str] = None
    raw: str = ""

def parse_command(user_input: str) -> Optional[Command]:
    text = user_input.strip().lower()
    if not text:
        return None

    parts = text.split()

    if len(parts) == 1 and parts[0] in DIRECTION_SYNONYMS:
        return Command(verb="go", target=DIRECTION_SYNONYMS[parts[0]], raw=user_input)

    verb = VERB_SYNONYMS.get(parts[0])
    if not verb:
        return Command(verb="unknown", raw=user_input)

    if verb == "go":
        if len(parts) > 1 and parts[1] in DIRECTION_SYNONYMS:
            return Command(verb="go", target=DIRECTION_SYNONYMS[parts[1]], raw=user_input)
        return Command(verb="go", raw=user_input)

    if verb in ["look", "take", "drop", "use", "unlock"]:
        obj = " ".join(parts[1:]) if len(parts) > 1 else None
        return Command(verb=verb, obj=obj, raw=user_input)

    return Command(verb=verb, raw=user_input)
