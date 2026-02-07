def main():
    df_to_csv()

def df_to_csv(df):
    df.to_csv("data/books.csv", index=False)
    
    
if __name__ == "__main__":
    main()
    

