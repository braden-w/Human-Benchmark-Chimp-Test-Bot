# Human-Benchmark-Chimp-Test-Bot
A Python Selenium bot which memorizes and plays the chimp test from https://humanbenchmark.com/tests/chimp. Before each round, the bot creates a dictionary of the numbered buttons with `number: location`, the memorization step. Afterwards, it seeks each button's location, using the `number` key to ensure they are completed in order.
