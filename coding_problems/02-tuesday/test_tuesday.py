import pytest

from tuesday import duplicate_count


def test_basic_test_1():
    assert duplicate_count("") == 0


def test_basic_test_2():
    assert duplicate_count("abcde") == 0


def test_basic_test_3():
    assert duplicate_count("abcdeaa") == 1


def test_basic_test_4():
    assert duplicate_count("abcdeaB") == 2


def test_basic_test_5():
    assert duplicate_count("Indivisibilities") == 2


@pytest.mark.parametrize("text,count",
                         [("Y1TlnXqW4hg5cC86rf0PGE1GNftHj9NX4B2s43Fa5n8zQdF0ugETwQbdwZFVOTRsff9GKguPRDCtJKakntfdYgIHUtgpRkVtfE", 28),
                          ("g0jcQwGeSU71cjbC5GEXScyb9An8fI", 6),
                             ("rQStbuDeO8N5LV5snjDDOQoHpnrvswXtmJGXDZ47Q1ntseT4S8sXWr6LIKnuLP", 18),
                             ("XnbV3RjRBIWtpjn1viujdmLjQtzVrzJEZ2wLacVVI7lwyfGFtEZU4UweSiuT9dusPNeXcFAj08dmDfHKPm082eqjkiFSfl", 25),
                             ("abTyy7K0JfuZRgq5BNG6mH6Ytyl5isbrSPc7d0t8c", 11),
                             ("QKfN3kdr6XPxImYfxAOD", 4),
                             ("a1X2L406fxZBb4U3uQDmg", 4),
                             ("TR4Psy2ru97aTIlkrxl6wEXUNldwz6ZCwnUFHjzW5DHkKf9nn3HdGGDfKmRHVJUsjQFYCVa", 21),
                             ("jxKfvl639rwYe", 0),
                             ("fWBAuV3WI8s2XwcjRYYOW7nhuJoojW0hjs5ueHsGjrKqRtsLFMk", 10),
                             ("pPYTfVrhO6U", 1),
                             ("J7w1MotUdd9Now0wyAdnRQMTcqSUse3VtT2coB0GLvSeN3o6ZZal4xUZsGnr2lR5LrWmUQM8K73a8SMzCicG18cwK", 24),
                             ("jQaVsuTKnlGRv28FFCjvNvS9Z83dgY", 7),
                             ("kg9zBuvvAUXW5F6Yyl01xfZwx7owPFsrSOah0bVw6K02SEnQGr2NxlNkEO", 20),
                             ("5natK03rKtBTb85hlIyxwne6JnaOXywcu2BXxSvULHPwYnSc5v", 15),
                             ("6JnToDAcgoEdViCZ", 3),
                             ("XEul1RNixHeuFgDC32RmjuwGUjtx3Ntrx42ER3Ih2zIUD8Gmc1sbL3M", 17),
                             ("tpDCL6GHGO2wPozueCB9ay", 4),
                             ("", 0),
                             ("PaV7pHF42gAdG1HRK", 4),
                             ("qWIeKrUTwNxC2hx56g5dLhAd", 5),
                             ("hdAZix8bKDninyCkSoO24EbMFOVN9Pu6gsww7fGlJQMyRiIfjXyAUunIlRNO1IxWbShmqddRLHG9aSVJtL4T", 24),
                             ("OuIj1hWRm3z93aE8Hetvx6bJYfanj2cpghBl1ZCpTfMW5fXouT", 17),
                             ("d9zEaljNr", 0),
                             ("89DVVhxhmjBUHc15DfY2l2qqzXJzQzPBS6cPfpGfzVzcn574hnRHDrF67bh5i8acNQqniehpI6xE9Ce", 21),
                             ("w18NoInjrrq", 2),
                             ("449QknjpxvkTyZH0OetIQMI3gURG2hAR2UODj0DZ9CnZzfz7nVUvZSOL10Qa0MfBMdwpbElMfRL", 25),
                             ("pJk7BZCAeRAVYYFCnC5uNb0OnAbbGfBvpfAzcOOjpl1DhKLHa8Xy2vO3GKDFjyZW12yIEPaf3Uc7YVMCRhrO07j", 24),
                             ("ynBtuac70NWmtLgs6cmXgoCm5dENajLLMjRF6VYlMZfNQ3gITHq4RFhVyiXaEBjg1rK9NePBKDBPbczTl7Zu", 25),
                             ("RIsX57pXMDNS8LDjMfjDAVsvqOxPI2KbPpkTPCS43QBzYMMCMRTwtLnCxwCDEuXI2evQPn5ONhOd2NqzXG6TDVfGA", 25),
                             ("fBmM1w9rdOaevDcM3MOlybwYwAP7dD3Jsccy7pPjo3yIVwEiPcliLXj3L7POjsQWtXdHCJNnBSSXqn3Pqx6srgbOi", 21),
                             ("rKsqmVzOcRCoG6m0ryYz9k5FRpc5KwoYM3KLWLfZSyAJrXMHz8bLYI5jdZEIH7X3dTfqx6yJX3zC3cgBisQ69M", 23),
                             ("uEXCEt8ZVvzrfGzTePwXZ3", 5),
                             ("UK1EsBp5BXDr2ZzpcUrQx3qyApDNclAT2Zl", 12),
                             ("NQqpysRmgm4egsObpj94zE7qC07SNrI77Uk1udSuGj2pGZ33nKnk2ySoHkBU16qqotgjUODF3092i9IDnMM50Z5e", 25),
                             ("b0OCk0zyIIAJDOFIdTuHAtb3C", 8),
                             ("4ZzQvDfIs2ejHSey7Xjdnclo4EMrNQ7wNLn7zO3urs", 12),
                             ("HCmbH4nYCjupKV8DxdfBO1hjw3dakb5XqkVzCYDX0IL4efZ", 12),
                             ("uw28pKl39sm6iz618GrOYXejVhD", 2),
                             ("w3mJUZyd087XVyEu1t8DTVbjT6IQBP5qsBoPUYAy4iMjq", 12),
                             ("K6slCE26NwffaTvOnMMOST8zPK2RBbRfjFVxlgxlGj9Ovtlb8aStuGx0g1eyAZmHR1Yfqt4BmhRUygBrtEzu", 24),
                             ("rhb1fWepVTRRqU0oNBBnItWYZjlrd9Q8VqdHwU2ANLB2GB5rPxCGLxVKKQR7jY", 18),
                             ("QNW66s79nQtErFLHK1Bme", 4),
                             ("b3GEGnKrVmTZiEzPIDO7BQPUsXSzZ3uaJe5XZZgsl6w9tAh7rLe5su1gkTrjzdmiIvUEc627YwxsEsFNVHHJvQQqJ5kRh", 26),
                             ("vGlW7EUFdFA7DcZUxDjFmU7KosAS9urnPyJIXc0CDTlYZkchEFLyxiVLpj6otjsKOXIO89pAeNfgf2gI1c", 22),
                             ("kUX0P01nBJYdBjpknyhvUcTXyfqTvpmA6kvmwDTlmhdhxJ04fYm09nfeZaNwxDSlIQ", 19),
                             ("ZtQTkt1LPYX8WnGs1QMLL4d6II8LIsG564mOo6", 12),
                             ("7YJEJXSulCsUbYZGXgvIeDhK67cqjJs3NUWBkqIF6NlbBk6jZdZMRHumKpX6sAxRTytef4emNLreHu", 23),
                             ("UCFebc0deKMkTL6iHIzJ7cZEmM8w8cTdbIIvRgbzNyjg1xoJLQABPvoNedH0TRQ90ib0X9Mkd0KXvVRQmZeSAh", 23),
                             ("LWNoxM", 0),
                             ("sSuMmcmDGXklx2y4ktX5XEB5UkkIK4l61jS1QDX0ivyxkLb", 13),
                             ("MlC2ZzCl7IEDFJiUBXrNYE9Pa4vKBdlCWWxhjRNw", 12),
                             ("Rg1OFJApXqlCisyIrlgyW0", 5),
                             ("tItTOAxhQKnpJB4XqERZNkAMyjLvTzUgcfAZmmB8dGN2D4os91BA4IkWxgxqXmOKTj2Aj9d8e", 19),
                             ("uLIxL1XMJ", 2),
                             ("mCIuQ1nP2G8Oe7b16rx6kjs57vYms0", 5),
                             ("Mk2EuFXTFNrQPZ0lBLebdC9fRcMtA84ZCb2aN1QwJnijNOgZBjW26ziPQSnQ", 17),
                             ("k6234TYw1NbH0PULlT1oaeB1yTgjCllEBdQ2uPdyO3G6kz9THJZGqWG2fpgYgUMtN", 21),
                             ("tMLeP6Bb7cIWG7OO0yc3m49lZpwnMB2seUvqz1UVM41jcTHWZZLi5J4S4IvWBBzwUAj3GdZtvA5gYnyF", 24),
                             ("QtnQQmJIQEbeCCqadXGx2d3QaLjmGedPHvN0j2PA4xdsL9Dm2KSIIwpI2nVVofbJyQ", 17),
                             ("DtQ7oU50EyGgJeM3uKGIHwUD14OLA6XI9", 6),
                             ("F4", 0),
                             ("zDJLCHGoTjKwZYBABsKCYSEOmaSU2rRI8MaIrofdCmJWxK1lLZM3Xkbz4Z5f7IaTGVg6vvG", 20),
                             ("MkbOMMr9ZxvaFK6sUq0V4PhCrtbPDaqwo6CG780K9M3oGeUnu443mcOGnft", 20),
                             ("DOGtLYpr7w9VGjRRWfTcUDyFGReOZvpZhgwNjdhvQ2262CmWmxFZ3u6zI5g7Ul4FiPGZrtmt6ZI1X55mU", 23),
                             ("me1oLPjvaVFewYJwXW2mwlrYltD5bBWpb65K5BzuYZMFuIOYZgguNcz99keyc6PMCLpAeovthNyuMWdV", 23),
                             ("FF6qiJ0CXQw3L83HmmXKdt4arU82", 6),
                             ("4JBV5f4u9NzCBGt1V9FR4kZPQHsYjSUr0XqJGdBcPQVjCH12wICYDIq88bY8P3u9Jq2CRgFITaUnitu7SRghPOuo0x2", 26),
                             ("hnTwHTeKAZW1eM5oRkAPNli9yQAPCzHfuHcaAWSxmVIw8yDBQ0K9DxFRzkIxJKjZ3Ca9d", 20),
                             ("nqxusptv3OqCzg", 1),
                             ("RoWZ5i5oA4OvIyjbFS1BDAb0o0ACZ7jShIvImlPjKg96LAw", 12),
                             ("6kWWc67eB4WSdYEjjBNT2GBeEJmmSydOxmGKqC8OBBKMpOe465LuIb6BJpBc2qTA3hWtJlDrXosN60", 21),
                             ("iSBpoIJDPwKBz9udG465tVIvJ", 6),
                             ("zOxhah1yguukKWOHRBrCAKp1qld7bHrHTpFZZ1IVUsLgBmCeSDM047ZNCbPMPMQRLNut0S5DAVY6hhNHLfML", 24),
                             ("NBXIHJ9YjW6nenDLNc1D8WK", 4),
                             ("WAT6aK4snNLos", 3),
                             ("SZlMtCcex0RqaBXIYx0wK0xhu05xPg4gGlfsfINy3m3vbT2JRKuEEndPVuO", 20),
                             ("rZNVckg8CJc9e7stgRQ", 3),
                             ("ep5B4Xx8mC6LWNs4D5j3Qp2A0jpedmiVaOYPJNFnnr5k7egch1w1JlTLmCOmkyIfth3ASKOU7fB", 25),
                             ("7tWDTy2sq02mD", 3),
                             ("Pdi", 0),
                             ("lpVdXpYZnHEO1GgSh3nGNd63UYdiQZigVl9rw", 11),
                             ("MyPvE8VSGU3IxJNKj0phwUUQPhkV3DlNmxmBxSrVzwiyhZxFxqReINaar", 19),
                             ("g", 0),
                             ("aYsLfsilmWPIVCzB3SuLo", 3),
                             ("osymVISiitvWUGelDBY9yI", 4),
                             ("9ZPxruywBFGpYmG1bBWLZj93C2G4iS9lHjJ1CSj9OJBOIDyP2sdmQj6vVEYuVU", 19),
                             ("yjcBmwBUyKbv61Nu1lowq5azxu2Z3ZmfafoNz", 11),
                             ("uHEaN5QMzpfncW2qqfLXPJFsvgq4XiWjvzH0Q6swRBPFFAZcusz6Sno2WMBJPzqAw4EvJt6ujR6ilt0Bbdbwl9zW2IMYgB0E71dr", 27),
                             ("oQ9wHj87T8n0HnRb5kK4IC217oqCkArB26ysNwgZH3XNYvgNcnzTZqgqu25XNuY", 19),
                             ("etVaUYLLYYDcgkHfU", 3),
                             ("TAOu8eDLd", 1),
                             ("hSSE0o4LzRK6trdHCtSXGcMm", 6),
                             ("E6u24whKQeDjg7fmLnnA1pLD", 4),
                             ("v9tLdcbld2KkaqzH587IQHYz1Bcx5B93yUlRoH1u3zSSYanaGwaHguFqyzwuurZeZefgqpWw47ZHF", 22),
                             ("QOmgIcfcURfQTycOR6EFCrSO5dKg4U1TRZC0McOtM0B8zsqBKvp5t23IBTvboAMtbe2GltRChblDrNums5yR5", 22),
                             ("g8u9", 0),
                             ("SYXKub9FSzeRX18alw4nZ7og8W1XN3FiF3apu6d2nLt9rEAEIey3OZer05NP4Cpm5hq8GlPOpWrO9iOdlC0YqlVGbztn7DW", 29),
                             ("1gWu4fSD9ewRZRTW9t6hr3C3j5Kp0eupgMJYMDkUF4Fvh82nq7JFUBWecKoqAGaeRgs1QPvRkcsn8ul", 24),
                             ("hSofQOnU6UHFndmzHmmnQ", 7)])
def test_random_test_cases(text, count):
    assert duplicate_count(text) == count
