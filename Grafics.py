# Save each plot as a separate PNG file

# Plot 1: Market Prices Over Time
plt.figure(figsize=(7, 5))
plt.plot(trees_df['DATA'], trees_df['OPEN'], label='Open', alpha=0.8)
plt.plot(trees_df['DATA'], trees_df['HIGH'], label='High', alpha=0.8)
plt.plot(trees_df['DATA'], trees_df['LOW'], label='Low', alpha=0.8)
plt.plot(trees_df['DATA'], trees_df['CLOSE'], label='Close', alpha=0.8)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Market Prices Over Time')
plt.legend()
plt.savefig('/mnt/data/market_prices_over_time.png')
plt.close()

# Plot 2: Pontos and Tot_Pontos Over Time
plt.figure(figsize=(7, 5))
plt.plot(trees_df['DATA'], trees_df['Pontos'], label='Pontos', color='purple', alpha=0.8)
plt.plot(trees_df['DATA'], trees_df['Tot_Pontos'], label='Total Points', color='orange', alpha=0.8)
plt.xlabel('Date')
plt.ylabel('Points')
plt.title('Pontos and Tot_Pontos Over Time')
plt.legend()
plt.savefig('/mnt/data/pontos_tot_pontos_over_time.png')
plt.close()

# Plot 3: Standard Deviations of Close Prices
plt.figure(figsize=(7, 5))
plt.plot(trees_df['DATA'], trees_df['SD_Close_5_N'], label='SD Close 5', alpha=0.7)
plt.plot(trees_df['DATA'], trees_df['SD_Close_10_N'], label='SD Close 10', alpha=0.7)
plt.plot(trees_df['DATA'], trees_df['SD_Close_20_N'], label='SD Close 20', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviations of Close Prices')
plt.legend()
plt.savefig('/mnt/data/standard_deviations_close_prices.png')
plt.close()

# Plot 4: High/Low to Close Ratios and Counts
plt.figure(figsize=(7, 5))
plt.plot(trees_df['DATA'], trees_df['COUNT_HiLo_N'], label='COUNT_HiLo_N', color='brown', alpha=0.7)
plt.plot(trees_df['DATA'], trees_df['HIGHtoCLOSESUMLAST10_N'], label='HIGHtoCLOSESUMLAST10_N', color='blue', alpha=0.7)
plt.plot(trees_df['DATA'], trees_df['LOWtoCLOSESUMLAST10_N'], label='LOWtoCLOSESUMLAST10_N', color='red', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Ratio/Count')
plt.title('High/Low to Close Ratios and Counts')
plt.legend()
plt.savefig('/mnt/data/high_low_close_ratios_counts.png')
plt.close()

# Provide file paths for download
file_paths = {
    "Market Prices Over Time": "/mnt/data/market_prices_over_time.png",
    "Pontos and Tot_Pontos Over Time": "/mnt/data/pontos_tot_pontos_over_time.png",
    "Standard Deviations of Close Prices": "/mnt/data/standard_deviations_close_prices.png",
    "High/Low to Close Ratios and Counts": "/mnt/data/high_low_close_ratios_counts.png"
}

file_paths
