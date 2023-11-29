import pkgutil

# Define a list of libraries you want to import with mnemonics
libraries = {
    "numpy": "np",
    "pandas": "pd",
    "matplotlib.pyplot": "plt",
    "sklearn": "skl"
    # Add more libraries here with their respective mnemonics
}

for lib_name, mnemonic in libraries.items():
    try:
        lib = __import__(lib_name)
        globals()[mnemonic] = lib
    except ImportError:
        print(f"Failed to import {lib_name}")

# Now you can use np, pd, plt, and skl as mnemonics for numpy, pandas, matplotlib.pyplot, and sklearn respectively
