# 🎲 Dungeon Dice: Trials of the Obsidian Keep — Full Game Blueprint

---

## **1. Title & Menu**

* **Game Title:** *Dungeon Dice: Trials of the Obsidian Keep*
* **Main Menu Options:**

  * `[1] Begin the Trials` → Start new game
  * `[2] View Legends` → Show high scores
  * `[3] Abandon Quest` → Exit program

---

## **2. Character Setup**

* Prompt player for **Name**
* Starting stats:

  * `Health = 100`
  * `Attack = 10`
  * `Inventory = []` (empty at start)

---

## **3. Dice Mechanics**

* Core mechanic: **six-sided die** (`1–6` random).
* **Room actions:**

  * Roll ≥ 4 → Success
  * Roll ≤ 3 → Failure
* **Combat actions:**

  * Player Attack = `Attack stat + dice roll (1–6)`
  * Boss Attack = fixed damage (20 each turn)

---

## **4. Rooms & Events (3 total)**

### **Room 1 — The Crumbling Corridor**

* Description: *“Dust fills the air. A cracked treasure chest glimmers faintly, while a collapsed passage might hide secrets.”*
* Choices:

  1. Open the chest

     * Success → Gain **Health Potion** (+25 HP, 1 use)
     * Failure → Trap triggers, **-10 HP**
  2. Clear rubble

     * Success → Gain **Ancient Amulet** (+5 Attack in boss fight)
     * Failure → Falling stones, **-15 HP**

---

### **Room 2 — The Spider Crypt**

* Description: *“Cobwebs coat the walls. A nest of shadow-spiders stirs. A forgotten satchel lies half-buried in bones.”*
* Choices:

  1. Raid the satchel

     * Success → Gain **Stamina Draught** (+15 HP when used)
     * Failure → Spider bite, **-12 HP**
  2. Burn the webs

     * Success → Find **Iron Dagger** (+3 Attack in boss fight)
     * Failure → Fire spreads wildly, **-10 HP**

---

### **Room 3 — The Hall of Echoes**

* Description: *“Your footsteps echo strangely. Two glowing doors appear: one radiates warmth, the other whispers cold promises.”*
* Choices:

  1. Enter warm door

     * Success → Find **Elixir of Vitality** (+20 HP)
     * Failure → Blinding light, **-15 HP**
  2. Enter cold door

     * Success → Find **Crystal Fang** (+5 Attack in boss fight)
     * Failure → Frost burns, **-10 HP**

---

## **5. Inventory System**

* Items stored in a list:

  * **Health Potion** → +25 HP (usable in boss fight)
  * **Stamina Draught** → +15 HP (usable in boss fight)
  * **Ancient Amulet** → +5 Attack (permanent, boss fight only)
  * **Iron Dagger** → +3 Attack (permanent, boss fight only)
  * **Crystal Fang** → +5 Attack (permanent, boss fight only)
* **Items are consumed** when used.

---

## **6. Boss Fight**

* Boss: **The Obsidian Warden**
* Description: *“A towering figure of molten stone and obsidian rises from the keep’s heart, wielding a fireblade.”*
* Stats:

  * Health = **200**
  * Attack = **20**

**Combat Loop:**

1. **Player Turn**

   * Options:

     * **Attack** → Damage = `player.attack + dice roll (1–6)`
     * **Use Potion/Draught** → Heal (if in inventory)
     * **Use Special Item** (Amulet, Dagger, Fang) → Buff attack permanently (+X), item removed from inventory
2. **Check Boss HP**

   * If ≤ 0 → Player wins
3. **Boss Turn**

   * Deals fixed **20 damage** to player
4. **Check Player HP**

   * If ≤ 0 → Player loses

Loop continues until one side’s HP = 0.

---

## **7. End Game & High Scores**

* **Victory Message:**
  *“You have conquered the Obsidian Warden! Your name shall be etched in legend.”*
* **Defeat Message:**
  *“Your bones join the countless others in the keep’s shadow…”*
* **Score = Player’s Remaining HP (if win)**
* **High Score Handling:**

  * Load from file if exists
  * Append new score
  * Sort descending
  * Save back to file
* **View Legends** shows sorted scores list
