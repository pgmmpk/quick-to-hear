import re


def main(infile):

    with open(infile) as f:
        text = f.read()

    text = re.sub(r'\n{2,}', '\n\n', text, flags=re.MULTILINE)
    text = re.sub(r'[ \t]+\n', '\n', text, flags=re.MULTILINE)
    text = re.sub(r'\n[ \t]+', '\n', text, flags=re.MULTILINE)

    blocks = text.split('\n\n')

    for b in blocks:
        if b.startswith('### '):
            yield f'<h3>{b[4:]}</h3>\n'
        elif b.startswith('## '):
            yield f'<h2>{b[3:]}</h2>\n'
        elif b.startswith('# '):
            yield f'<h1>{b[2:]}</h1>\n'
        elif b.startswith('**') and b.endswith('**'):
            yield f'<i>{b[2:-2]}</i>\n'
        else:
            yield f'<p>{b}</p>'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser('md2html')
    parser.add_argument('infile', help='Input Markdown file')

    args = parser.parse_args()

    print('<html><head>')
    print('<link href="https://fonts.googleapis.com/css2?family=PT+Sans" rel="stylesheet">')
    print('<link type="text/css" rel="stylesheet" href="./common.css">')
    print('</head><body>')
    for block in main(args.infile):
        print(block)
    print('</body>')
