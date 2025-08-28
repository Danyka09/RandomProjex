## **1. Setup**

* [ ] Print title + main menu

  * `[1] Start New Game`
  * `[2] View Leaderboard`
  * `[3] Quit`
* [ ] Prompt player for name
* [ ] Initialize starting stats:

  * HP = 100
  * Inventory = 3x Healing Potions (+30 HP each)
* [ ] Create dice roll mechanic (D6 → damage values table)

---

## **2. Planet Battles**

### **Planet Apollo** (HP = 100)

* [ ] Describe planet + enemy (archers)
* [ ] Loop: roll D6 → apply damage (player vs. planet HP)
* [ ] On victory → reward 🎯 **Bow** (2 arrows, \~2× damage, limited uses)

---

### **Planet Groverland** (HP = 130)

* [ ] Describe planet + enemy (satyrs + demigods)
* [ ] Combat loop (D6 system again)
* [ ] On victory → reward ✒️ **PenSword** (boss-only, 3× dmg, heal 25 HP, single use)

---

### **Planet Delta** (HP = 150)

* [ ] Describe planet + enemy (robots + lasers)
* [ ] Combat loop (D6 system)
* [ ] On victory → reward 🔫 **Laser Gun** (40 dmg, costs 5 HP per shot, \~3 uses)

---

## **3. Boss Fight**

* [ ] Decide **which boss to load**:

  * If leaderboard empty → Boss = Zlorg (200 HP)
  * Else → Boss = Current Emperor (top leaderboard entry, HP 200, Attack \~20)
* [ ] Describe boss intro (Zlorg vs. Player Emperor flavor text)
* [ ] Fight loop:

  * Player’s turn → \[Attack / Use Item / Heal]
  * Boss’s turn → fixed damage (20)
* [ ] Items work as follows:

  * 🎯 Bow → 2× damage, 2 uses
  * ✒️ PenSword → 3× damage + heal 25, 1 use, boss only
  * 🔫 Laser Gun → 40 dmg, −5 HP, 3 uses
  * Potions → +30 HP, 3 uses at start

---

## **4. Endgame**

* [ ] Check HP outcomes

  * If player dies → defeat message
  * If boss dies → victory message
* [ ] Calculate final score = Remaining HP + leftover item value
* [ ] Prompt for name → add to leaderboard

---

## **5. Leaderboard System**

* [ ] Load leaderboard from file at start (if file exists)
* [ ] After victory:

  * Append `{name, score}` to list
  * Sort descending by score
  * Save back to file
* [ ] On “View Leaderboard” → print sorted list
* [ ] Emperor = top entry
* [ ] (Optional) Menu toggle: *“Fight Zlorg instead of current Emperor?”*

---

✅ **Order of coding**:

1. Setup (menu, name, stats, dice)
2. One planet (Apollo) → test full loop
3. Add other planets (Groverland, Delta)
4. Boss fight system (start with Zlorg only)
5. Expand boss fight → Emperor system
6. Endgame messages + scoring
7. Leaderboard load/save/display
8. Polish (flavor text, balance, optional Emperor toggle)



#use ~~ to cross out