using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;
using OpenQA.Selenium.Interactions;
using System;
using System.Collections.Generic;

namespace SeleniumCSsharp
{
    public class Tests
    {
        IWebDriver driver;
        string test_url = "https://vjatseslavaktsurin22.thkit.ee/wp/";

        [SetUp]
        public void StartBrowser()
        {
            driver = new FirefoxDriver(@"C:\Users\opilane\source\repos\Selenium\driver\");
            driver.Manage().Window.Maximize();
        }

        [Test]
        public void TestMenuFocus()
        {
            driver.Url = test_url;
            driver.Navigate().GoToUrl("https://vjatseslavaktsurin22.thkit.ee/wp/");

            
            var menuButton = driver.FindElement(By.ClassName("colibri-menu-container"));

            
            menuButton.Click();

            
            Thread.Sleep(2000);

            
            var menuItems = driver.FindElements(By.XPath("//ul[@id='menu-main']/li"));

            
            Actions actions = new Actions(driver);
            bool allLinksNonEmpty = true;


            foreach (var menuItem in menuItems)
            {
                actions.MoveToElement(menuItem).Build().Perform();
                Thread.Sleep(1000);
                                var link = menuItem.FindElement(By.TagName("a"));
                var href = link.GetAttribute("href");
                if (string.IsNullOrEmpty(href))
                {
                    allLinksNonEmpty = false;
                    break;
                }
            }

            if (allLinksNonEmpty)
            {
                Console.WriteLine("GREAT");
            }
            
        }

        [TearDown]
        public void CloseBrowser()
        {
            driver.Quit();
        }
    }
}
