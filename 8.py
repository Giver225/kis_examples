def main(row):
    ans = {}
    row = row.replace('\n', ' ')
    row = row.replace('<section>', '')
    row = row.replace('q(', '')
    row = row.replace('(', '')
    row = row.replace(')', '')
    row = row.replace('</section>', '')
    row = row.replace('var', '')
    row = row.replace('.', '')
    row = row.replace('"', '')
    row = row.replace(' ', '')
    row = row.split(';')
    row.pop()
    for i in row:
        i = i.split('=:')
        ans |= {i[1]: i[0]}
    return ans


if __name__ == '__main__':
    print(main('''<section> ((var q(usis) =: "teriso".)); ((var q(vear)=:"dive".));((
    var q(bigeon) =: "belais_152". )); ((var q(isdi_230) =: "diinre". ));
    </section>'''))
