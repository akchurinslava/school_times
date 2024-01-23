﻿using System;
using System.Collections.Generic;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace mobile_app
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class StepperSliderPage : ContentPage
	{
		Stepper stepper;
		Slider slider;
		Label label;
		public StepperSliderPage()
		{
			//InitializeComponent ();
			label = new Label
			{
				Text = "...",
				HorizontalOptions = LayoutOptions.Center,
				VerticalOptions = LayoutOptions.Center,

			};

			slider = new Slider
			{
				Minimum = 0,
				Maximum = 100,
				Value = 50,
			};
            slider.ValueChanged += Slider_ValueChanged;

			stepper = new Stepper
			{
				Minimum = 0,
				Maximum = 100,
				Increment = 5,
				HorizontalOptions = LayoutOptions.Center,
				VerticalOptions = LayoutOptions.Center
			};
            stepper.ValueChanged += Stepper_ValueChanged;

			StackLayout st = new StackLayout
			{
				Children = {slider, stepper, label}

			};
			Content = st;

		}

        private void Stepper_ValueChanged(object sender, ValueChangedEventArgs e)
        {
			label.Text = String.Format("Oli valitud: {0:F1}", e.NewValue);
			label.FontSize = e.NewValue;
            slider.Value = e.NewValue;
            //label.Rotation = e.NewValue;
        }

        private void Slider_ValueChanged(object sender, ValueChangedEventArgs e)
        {
            label.Text = String.Format("Oli valitud: {0:F1}", e.NewValue);
            label.FontSize = e.NewValue;
            stepper.Value = e.NewValue;
            //label.Rotation = e.NewValue;
        }
    }
}

