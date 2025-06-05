public class ExampleController : Controller
{
    public void Run(string message)
    {
        // Sanitize the input to prevent code injection
        message = Microsoft.Security.Application.Encoder.EncodeForHTML(message);

        const string code = @"
            using System;
            public class MyClass
            {
                public void MyMethod()
                {
                    Console.WriteLine(""" + message + @""");
                }
            }
        ";

        // Use a temporary file instead of compiling from a string
        string tempFile = Path.GetTempFileName() + ".cs";
        File.WriteAllText(tempFile, code);

        var provider = CodeDomProvider.CreateProvider("CSharp");
        var compilerParameters = new CompilerParameters
        {
            ReferencedAssemblies = { "System.dll", "System.Runtime.dll" },
            GenerateExecutable = false,
            GenerateInMemory = true
        };

        CompilerResults compilerResults;
        using (var sourceFile = new StreamReader(tempFile))
        {
            compilerResults = provider.CompileAssemblyFromSource(compilerParameters, sourceFile.ReadToEnd());
        }

        if (compilerResults.Errors.Count == 0)
        {
            object myInstance = compilerResults.CompiledAssembly.CreateInstance("MyClass");
            myInstance.GetType().GetMethod("MyMethod").Invoke(myInstance, new object[0]);
        }
        else
        {
            // Handle compilation errors
        }

        // Clean up the temporary file
        File.Delete(tempFile);
    }
}