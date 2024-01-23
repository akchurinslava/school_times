using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app 
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class BoxViewPage : ContentPage
    {
        Label label;
        public BoxViewPage()
        {
            //InitializeComponent();

            label = new Label
            {
                Text = "Click count",
                HorizontalOptions = LayoutOptions.CenterAndExpand,
                VerticalOptions = LayoutOptions.CenterAndExpand,
            };


            Button clk = new Button
            {
                Text= "CLICK",
                HorizontalOptions = LayoutOptions.CenterAndExpand,
                VerticalOptions = LayoutOptions.CenterAndExpand,
            };

            StackLayout st = new StackLayout
            {
                Orientation = StackOrientation.Vertical,
                Children = { label, clk },
                BackgroundColor = Color.Bisque
            };

            clk.Clicked += Clk_Clicked;

            Content = st;

        }

        private int ChangeSize()
        {
            var random = new Random();
            List<int> sizes = new List<int> {30, 50, 40, 45, 20, 30, 40};
            int index = random.Next(sizes.Count);
            return sizes[index];
        }

        int i = 0;
        private void Clk_Clicked(object sender, EventArgs e)
        {
            i++;
            label.Text = i.ToString();
            label.FontSize = ChangeSize();
        }
    }
}