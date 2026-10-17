"""
Task 1: Analyze a CSV dataset and produce charts and summary statistics
Skills: Pandas, Matplotlib, Seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_and_explore_data(filename):
    """Load CSV data and display basic information"""
    print("="*60)
    print("LOADING AND EXPLORING DATA")
    print("="*60)
    
    df = pd.read_csv(filename)
    
    print("\n1. First few rows of the dataset:")
    print(df.head())
    
    print("\n2. Dataset shape:")
    print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n3. Data types:")
    print(df.dtypes)
    
    print("\n4. Missing values:")
    print(df.isnull().sum())
    
    return df

def calculate_statistics(df):
    """Calculate and display summary statistics"""
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    
    print("\n1. Numerical columns statistics:")
    print(df.describe())
    
    print("\n2. Department distribution:")
    print(df['Department'].value_counts())
    
    print("\n3. Average salary by department:")
    dept_salary = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
    print(dept_salary)
    
    print("\n4. Correlation between numeric variables:")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    print(df[numeric_cols].corr()['Salary'].sort_values(ascending=False))
    
    return df

def create_visualizations(df):
    """Create various charts and visualizations"""
    print("\n" + "="*60)
    print("CREATING VISUALIZATIONS")
    print("="*60)
    
    # Create a figure with multiple subplots
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Salary distribution histogram
    plt.subplot(3, 3, 1)
    plt.hist(df['Salary'], bins=15, color='skyblue', edgecolor='black')
    plt.title('Salary Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Salary ($)')
    plt.ylabel('Frequency')
    
    # 2. Box plot of salary by department
    plt.subplot(3, 3, 2)
    df.boxplot(column='Salary', by='Department', ax=plt.gca())
    plt.title('Salary by Department', fontsize=12, fontweight='bold')
    plt.suptitle('')
    plt.xlabel('Department')
    plt.ylabel('Salary ($)')
    
    # 3. Average salary by department (bar chart)
    plt.subplot(3, 3, 3)
    dept_avg = df.groupby('Department')['Salary'].mean().sort_values()
    dept_avg.plot(kind='barh', color='coral')
    plt.title('Average Salary by Department', fontsize=12, fontweight='bold')
    plt.xlabel('Average Salary ($)')
    plt.ylabel('Department')
    
    # 4. Scatter plot: Years of Experience vs Salary
    plt.subplot(3, 3, 4)
    plt.scatter(df['Years_Experience'], df['Salary'], alpha=0.6, c='green', s=100)
    plt.title('Experience vs Salary', fontsize=12, fontweight='bold')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary ($)')
    
    # 5. Performance score distribution
    plt.subplot(3, 3, 5)
    plt.hist(df['Performance_Score'], bins=10, color='lightgreen', edgecolor='black')
    plt.title('Performance Score Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Performance Score')
    plt.ylabel('Frequency')
    
    # 6. Age distribution
    plt.subplot(3, 3, 6)
    plt.hist(df['Age'], bins=12, color='orange', edgecolor='black')
    plt.title('Age Distribution', fontsize=12, fontweight='bold')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    # 7. Department distribution (pie chart)
    plt.subplot(3, 3, 7)
    dept_counts = df['Department'].value_counts()
    plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Department Distribution', fontsize=12, fontweight='bold')
    
    # 8. Correlation heatmap
    plt.subplot(3, 3, 8)
    numeric_cols = ['Age', 'Salary', 'Years_Experience', 'Performance_Score']
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, square=True, 
                linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Heatmap', fontsize=12, fontweight='bold')
    
    # 9. Performance vs Salary scatter
    plt.subplot(3, 3, 9)
    plt.scatter(df['Performance_Score'], df['Salary'], alpha=0.6, c='purple', s=100)
    plt.title('Performance vs Salary', fontsize=12, fontweight='bold')
    plt.xlabel('Performance Score')
    plt.ylabel('Salary ($)')
    
    plt.tight_layout()
    plt.savefig('Day1/analysis_charts.png', dpi=300, bbox_inches='tight')
    print("\n✓ Charts saved as 'analysis_charts.png'")
    
    # Create additional detailed visualizations
    fig2, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Violin plot for salary by department
    sns.violinplot(data=df, x='Department', y='Salary', ax=axes[0, 0], palette='Set2')
    axes[0, 0].set_title('Salary Distribution by Department (Violin Plot)', fontweight='bold')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Regression plot: Experience vs Salary
    sns.regplot(data=df, x='Years_Experience', y='Salary', ax=axes[0, 1], 
                scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    axes[0, 1].set_title('Experience vs Salary (with trend line)', fontweight='bold')
    
    # Count plot for department
    sns.countplot(data=df, x='Department', ax=axes[1, 0], palette='pastel')
    axes[1, 0].set_title('Employee Count by Department', fontweight='bold')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # Box plot for age by department
    sns.boxplot(data=df, x='Department', y='Age', ax=axes[1, 1], palette='husl')
    axes[1, 1].set_title('Age Distribution by Department', fontweight='bold')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('Day1/detailed_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Detailed charts saved as 'detailed_analysis.png'")
    
    plt.close('all')

def main():
    """Main function to run the analysis"""
    print("\n" + "="*60)
    print("CSV DATA ANALYSIS - TASK 1")
    print("="*60)
    
    # Load and explore data
    df = load_and_explore_data('Day1/sample_data.csv')
    
    # Calculate statistics
    df = calculate_statistics(df)
    
    # Create visualizations
    create_visualizations(df)
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print("\nKey Findings:")
    print(f"1. Total employees analyzed: {len(df)}")
    print(f"2. Average salary: ${df['Salary'].mean():,.2f}")
    print(f"3. Salary range: ${df['Salary'].min():,.2f} - ${df['Salary'].max():,.2f}")
    print(f"4. Average experience: {df['Years_Experience'].mean():.1f} years")
    print(f"5. Average performance score: {df['Performance_Score'].mean():.2f}/10")
    print(f"6. Highest paying department: {df.groupby('Department')['Salary'].mean().idxmax()}")
    print("\n✓ All visualizations saved in Day1 folder")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
