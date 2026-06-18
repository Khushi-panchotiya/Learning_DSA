# 1344. Angle Between Hands of a Clock | O(1) Math Solution | Beat 100% Runtime 🚀

## Intuition

A clock forms a full circle of **360°**.

- The **minute hand** completes a full rotation in **60 minutes**, so it moves **6° per minute**.
- The **hour hand** completes a full rotation in **12 hours**, so it moves **30° per hour** and **0.5° per minute**.

By calculating the positions of both hands and finding the difference between their angles, we can determine the angle formed between them. Since a clock can form two angles, we return the **smaller one**.

---

## Approach

1. Convert `hour` into a 12-hour format using `hour %= 12`.
2. Calculate the angle of the minute hand:
   - `minuteAngle = minutes * 6`
3. Calculate the angle of the hour hand:
   - `hourAngle = hour * 30 + minutes * 0.5`
4. Find the absolute difference between the two angles.
5. Return the smaller angle:
   - `min(diff, 360 - diff)`

---

## Complexity

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

---

## Code

```cpp
class Solution {
public:
    double angleClock(int hour, int minutes) {

        hour %= 12;

        double hourMovementPerMinute = 0.5;

        double minAngle = minutes * 6;

        double hAngle = hour * 30 + minutes * hourMovementPerMinute;

        double diff = abs(hAngle - minAngle);

        return min(diff, 360 - diff);
    }
};
```

### Key Observation

- Minute hand moves **6° per minute**
- Hour hand moves **0.5° per minute**
- The required answer is always the **smaller angle**, which is why we return:

```cpp
min(diff, 360 - diff);
```
