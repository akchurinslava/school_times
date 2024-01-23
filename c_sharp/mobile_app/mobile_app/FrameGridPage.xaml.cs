using System;
using System.Collections.Generic;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class FrameGridPage : ContentPage
    {
        Label lbl;
        Random rnd = new Random();
        public FrameGridPage()
        {
            //InitializeComponent ();
            //Frame frame;
            Grid grid;
            Button btn;

            //frame = new Frame
            //{


            //	BorderColor = Color.White,
            //	CornerRadius = 10,
            //	BackgroundColor = Color.FromRgb(rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)),

            //};

            //grid = new Grid
            //{
            //	RowDefinitions = 
            //		{
            //                     new RowDefinition{Height = new GridLength(1, GridUnitType.Star)},
            //                     new RowDefinition{Height = new GridLength(1, GridUnitType.Star)},
            //                     new RowDefinition{Height = new GridLength(1, GridUnitType.Star)}
            //                 },
            //	ColumnDefinitions = 
            //		{
            //			new ColumnDefinition{Width = new GridLength(1, GridUnitType.Star)},
            //                     new ColumnDefinition{Width = new GridLength(1, GridUnitType.Star)},

            //                 }

            //};

            //grid.Children.Add(frame, 0, 0);
            //grid.Children.Add(frame, 1, 0);
            //grid.Children.Add(frame, 0, 1);
            //         grid.Children.Add(frame, 1, 1);
            //         grid.Children.Add(frame, 0, 2);
            //         grid.Children.Add(frame, 1, 2);
            //Content = grid;

            grid = new Grid
            {
                VerticalOptions = LayoutOptions.FillAndExpand,
                HorizontalOptions = LayoutOptions.FillAndExpand,


            };

            //grid.RowDefinitions.Add(new RowDefinition { Height = new GridLength(1, GridUnitType.Star) });
            //grid.ColumnDefinitions.Add(new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) });

            for (int i = 0; i < 2; i++)
            {
                //grid.ColumnDefinitions.Add(new ColumnDefinition { Width = new GridLength(i + 1, GridUnitType.Star) });
                for (int j = 0; j < 3; j++)
                {
                    //grid.RowDefinitions.Add(new RowDefinition { Height = new GridLength(j + 1, GridUnitType.Star) });
                    grid.Children.Add(
                        btn = new Button
                        {
                            Text = i.ToString() + j.ToString(),
                            BorderColor = Color.White,
                            CornerRadius = 10,
                            BackgroundColor = Color.FromRgb(rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)),
                        }, i, j);
                    btn.Clicked += Btn_Clicked;
                }
            }
            lbl = new Label { Text = " ", BackgroundColor = Color.AliceBlue };
            grid.Children.Add(lbl, 0, 3);
            Grid.SetColumnSpan(lbl, 2);

            Content = grid;
        }

        bool klik = false;
        private void Btn_Clicked(object sender, EventArgs e)
        {
            List<Color> colors = new List<Color> { Color.Red, Color.FromRgb(rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)) };
            Button btn = sender as Button;
            //btn.BackgroundColor = Color.Red;
            //lbl.Text = btn.Text;
            var r = Grid.GetRow(btn);
            var c = Grid.GetColumn(btn);

            if (klik)
            {
                btn.BackgroundColor = Color.Red;
                klik = false;
            }
            else if (klik == false)
            {
                btn.BackgroundColor = Color.FromRgb(rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255));
                klik = true;

            }
            lbl.Text = r.ToString() + c.ToString();


        }
    }
}