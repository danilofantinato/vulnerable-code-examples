using System.Web;
using System.Web.Mvc;

public class ExampleController : Controller
{
    private readonly string[] _allowedDomains = { "example.com", "example.org" };

    [HttpGet]
    public ActionResult Redirect(string url)
    {
        if (string.IsNullOrEmpty(url))
            return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

        var uri = new Uri(url, UriKind.Absolute);
        var allowedDomain = _allowedDomains.Any(d => uri.Host.EndsWith(d, StringComparison.OrdinalIgnoreCase));

        if (allowedDomain)
            return Redirect(uri.ToString());
        else
            return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
    }
}