"""Run with: python -m unittest test_word_analyser -v"""

import contextlib
import io
import unittest
from unittest.mock import patch

import word_analyser as analyser


class WordAnalyserTests(unittest.TestCase):
    def test_sample_sentence(self):
        words = analyser.clean_text("Python is fun and python is useful")
        self.assertEqual(analyser.count_words(words), 7)
        self.assertEqual(analyser.count_unique_words(words), 5)
        frequencies = analyser.count_word_frequency(words)
        self.assertEqual(frequencies, {
            "python": 2, "is": 2, "fun": 1, "and": 1, "useful": 1,
        })
        self.assertEqual(analyser.find_most_common_word(frequencies), "python")
        self.assertEqual(analyser.find_longest_word(words), "python")

    def test_punctuation_and_whitespace_separate_words(self):
        self.assertEqual(
            analyser.clean_text("  Hello,world!\nHELLO\twell-known—words "),
            ["hello", "world", "hello", "well", "known", "words"],
        )

    def test_apostrophes_numbers_and_unicode(self):
        self.assertEqual(
            analyser.clean_text("Don't café 123 Python3"),
            ["don", "t", "café", "123", "python3"],
        )

    def test_empty_inputs(self):
        for text in ("", " \t\n", "!?—..."):
            with self.subTest(text=text):
                words = analyser.clean_text(text)
                self.assertEqual(words, [])
                self.assertEqual(analyser.count_words(words), 0)
                self.assertEqual(analyser.count_unique_words(words), 0)
                self.assertEqual(analyser.count_word_frequency(words), {})
                self.assertIsNone(analyser.find_most_common_word({}))
                self.assertIsNone(analyser.find_longest_word(words))

    def test_winners_can_appear_later(self):
        words = ["cat", "elephant", "dog", "dog"]
        self.assertEqual(analyser.find_longest_word(words), "elephant")
        self.assertEqual(
            analyser.find_most_common_word(analyser.count_word_frequency(words)),
            "dog",
        )

    def test_ties_choose_first_word(self):
        words = ["dog", "cat", "cat", "dog"]
        self.assertEqual(analyser.find_longest_word(words), "dog")
        self.assertEqual(
            analyser.find_most_common_word(analyser.count_word_frequency(words)),
            "dog",
        )

    def test_cli_report(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="Hi hi there!"), contextlib.redirect_stdout(output):
            analyser.main()
        for expected in (
            "Total words: 3", "Unique words: 2",
            "Most common word: hi (2 occurrences)",
            "Longest word: there (5 characters)", "  hi: 2", "  there: 1",
        ):
            self.assertIn(expected, output.getvalue())

    def test_cli_empty_input(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="!!!"), contextlib.redirect_stdout(output):
            analyser.main()
        self.assertIn("No words found", output.getvalue())

    def test_cli_cancellation(self):
        for error in (EOFError, KeyboardInterrupt):
            with self.subTest(error=error):
                output = io.StringIO()
                with patch("builtins.input", side_effect=error), contextlib.redirect_stdout(output):
                    analyser.main()
                self.assertIn("Analysis cancelled.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
