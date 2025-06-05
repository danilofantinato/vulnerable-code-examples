protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
{
    string connectionString = "Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=securePassword123!@#";
    optionsBuilder.UseSqlServer(connectionString);
}