---
title: "Devlog 1: Making my Pomodoro CLI glamorous with BubbleTea"
date: 2025-09-06
description: "Welcome to my first devlog for the Pomoloco app."
summary: "Learn more about my progress on my Pomoloco app written in Go with BubbleTea, Cobra, and Viper."
tags: ["welcome", "devlog", "go", "bubbletea"]
---
# Devlog 1: Glamorous TUI & Dynamic Quotes

## 🚀 So what did I do?
- Upgraded CLI app to a full TUI using **BubbleTea**. 
- Added configuration & flag handling with **Viper + Cobra**, required some refactoring. 
- Integrated **zenquote.io** so the app now displays inspirational quotes.
- Updated model initialisation so quotes refresh dynamically without blocking the UI.

## 🧩 What were the challenges / learnings?
- Understanding each tool and how they fit together was tricky for my first time working with this tech stack.
- Familiartity with Model View Update helped with using BubbleTea. It is based on the Elm architecture and I have used the paradigm before.
- The mose exciting for me, somehow, was updating the model’s `quote` property asynchronously and triggering a **Tea command** to trigger an update in the model and the view, rather than blocking on HTTP requests.  

## 🎯 What's next?
- Finish refactoring TUI components OUTSIDE Cobra/Viper components.
- Improve UI layout & styling for unsupported commandline emulators (like qrxvt).
- Add caching for fetched quotes to reduce API calls and allow for quotes in offline-mode.
- Add storage of usage data (like Title, Description, Quotes, and Session Notes) with **SQLite**.
