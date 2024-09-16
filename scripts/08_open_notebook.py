import subprocess
import os

def main():
    notebook_path = os.path.join('notebook', '08_Data_Visualization.ipynb')
    subprocess.run(['jupyter', 'notebook', notebook_path])

if __name__ == '__main__':
    main()
