def analyze_bwa(df):
    df.columns = ['Position', 'Wert']
    df['Position'] = df['Position'].astype(str).str.lower()
    result = {}

    def find_value(keywords):
        for keyword in keywords:
            row = df[df['Position'].str.contains(keyword)]
            if not row.empty:
                return float(row['Wert'].values[0])
        return None

    rohertrag = find_value(['rohertrag'])
    personalkosten = find_value(['personalkosten'])
    raumkosten = find_value(['raumkosten'])
    gewinn = find_value(['gewinn', 'jahresüberschuss'])

    if gewinn is None and rohertrag is not None:
        kosten = sum(filter(None, [personalkosten, raumkosten]))
        gewinn = rohertrag - kosten

    result['Rohertrag'] = rohertrag
    result['Personalkosten'] = personalkosten
    result['Raumkosten'] = raumkosten
    result['Gewinn'] = gewinn
    result['Kapitaldienstfähig'] = gewinn >= 2500 if gewinn is not None else False

    return result