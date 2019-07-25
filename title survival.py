def title_survival(df):
	return df[["Title", "Survived"]].groupby(['Title'], as_index=False).mean().sort_values(by='Survived', ascending=False)
	
def get_output_schema():
    return pd.DataFrame({
		'Title':prep_string(),
		'Survived':prep_decimal(),
    })