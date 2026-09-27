# PySideCourseStarterKit — Type Along with the PySide6 Decks

This project is the **starter kit** for the PySide6 slide decks (the
supplementary block "GUI Programming with PySide6" — 11 optional full-day
sessions, delivered after Week 24). It has exactly the same
layout as the completed `PySideCourse` project, but each file contains
only the code from the *previous* sessions already filled in; the code
that is *new* in a session is replaced by short `# TODO:` markers that
name the step, so you can type it yourself while following the deck.

The completed [`PySideCourse`](../PySideCourse) project is the reference:
if you get stuck, look there — every starter file mirrors its completed
counterpart one-to-one.

Each `sessionNN_*.py` module belongs to one deck (topic) of the course and
says so in its module docstring. Every file runs as-is (the TODO stubs do
nothing but never raise), so you can always execute your work in progress.

## Setup

```bash
pip install -r requirements.txt
```

(or `uv pip install -r requirements.txt` in a uv-managed environment)

## Running the examples

Run the scripts from this directory. Every script opens real windows on
your desktop:

```bash
python session01_first_window.py
```

| Deck (topic) | Files |
|---|---|
| The Event Loop and Your First Window | `session01_first_window.py`, `session01_greeter_form.py` |
| Signals and Slots | `session02_first_connection.py`, `session02_greeter_live.py`, `session02_slider_spinbox.py`, `session02_greeter_class.py`, `session02_custom_signals.py` |
| Layouts and a Widget Tour | `session03_greeter_layouts.py`, `session03_layout_gallery.py`, `session03_widget_tour.py` |
| Main Windows and Dialogs | `session04_text_editor.py`, `session04_dialogs.py` |
| Model/View Programming I | `session05_list_model.py` |
| Model/View II: Custom Models | `session06_student_model.py`, `session06_students_window.py`, `test_student_model.py` |
| Undo with the Command Pattern | `session07_undo.py` |
| Custom Widgets and Painting | `session08_canvas_basics.py`, `session08_drawing_canvas.py` |
| Long-Running Tasks | `session09_freeze_demo.py`, `session09_timer_chunking.py`, `session09_worker.py` |
| Persistence and Polish | `session10_drawing_app.py` |
| Workshops (starters) | `workshop01_profile_card.py`, `workshop02_temperature.py`, `workshop03_settings.py`, `workshop05_address.py`, `workshop09_file_processor.py`; workshops 4/6/7/8/10 build on the session files above |

## Notes

- `session06_students_window.py` imports from `session06_student_model.py`
  and therefore must be run from this directory.
- `test_student_model.py` is a pytest module (no GUI) and is **given**, not
  typed: it is the verification material for your `StudentModel`
  implementation — `pytest test_student_model.py`. The tests fail until you
  fill in the TODOs in `session06_student_model.py`.
- `session09_freeze_demo.py` freezes the UI for ~10 seconds **on purpose**
  once you fill in the TODO — that is the demonstration.
- The icons under `icons/` and the generated `resources_rc.py` (Qt resource
  system, session 10) are already built. To regenerate them:
  `python make_icons.py` then `pyside6-rcc resources.qrc -o resources_rc.py`.
- The completed project (`PySideCourse`) is the reference implementation;
  the capstone project (diagram editor) is a separate, installable package:
  `PySideDiagramEditor`.
