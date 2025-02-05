# Flash Card Program

A simple Python flash card application that helps you learn French words and their English translations.

## Overview

This project uses the Tkinter library for the graphical user interface (GUI). When you start the program, a French word is displayed on a flash card. After a few seconds, the card flips to reveal the English translation. You can then mark whether you got the word right or wrong, which updates the list of words to learn.


## Customization

- **Changing the Dataset:** Replace `data/french_words.csv` with your own CSV file of word pairs. Ensure the columns are labeled "French" and "English".
- **Timing Adjustments:** Modify the `window.after(3000, flip_card)` call to change the delay time before the card flips.
- **UI Customization:** Modify fonts, colors, and images to adjust the look and feel of the application.

## Conclusion

This Flash Card Program is a practical tool for language learners. Feel free to modify and expand the project to suit your needs. Enjoy learning French with interactive flash cards!
