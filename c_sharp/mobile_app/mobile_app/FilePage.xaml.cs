using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Xamarin.Forms;

namespace mobile_app
{	
	public partial class FilePage : ContentPage
    {
        string folderPath = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
        public FilePage ()
		{
			InitializeComponent ();
            
		}

        

        protected override void OnAppearing()
        {
            base.OnAppearing();
            UpdateFileList();
        }

        private void UpdateFileList()
        {
            //get all files
            filesList.ItemsSource = Directory.GetFiles(folderPath).Select(f => Path.GetFileName(f));
            //deselect
            filesList.SelectedItem = null;
        }

        async void Button_Clicked(System.Object sender, System.EventArgs e)
        {
            string filename = fileNameEntry.Text;
            if (String.IsNullOrEmpty(filename)) return;
            //if file exists
            if (File.Exists(Path.Combine(folderPath, filename)))
            {
                //request rewrite access
                bool isRewrited = await DisplayAlert("Kinnitus", "Fail on juba olemas, kas salvestada umber?", "Jah", "Ei");
                if (isRewrited == false) return;
	        }

            //rewrite file
            File.WriteAllText(Path.Combine(folderPath, filename), textEditor.Text);
            //refresh file list
            UpdateFileList();
        }

        void filesList_ItemSelected(System.Object sender, Xamarin.Forms.SelectedItemChangedEventArgs e)
        {
            if (e.SelectedItem == null) return;
            //get selected element
            string filename = (string)e.SelectedItem;
            //download text into text area
            textEditor.Text = File.ReadAllText(Path.Combine(folderPath, (string)e.SelectedItem));
            //set file name
            fileNameEntry.Text = filename;
            //deselect
            filesList.SelectedItem = null;
        }

        //void MenuItem_Clicked(System.Object sender, System.EventArgs e)
        //{
        //    //get name of file
        //    string filename = (string)((MenuItem)sender).BindingContext;
        //    //delete file from lisi
        //    File.Delete(Path.Combine(folderPath, filename));
        //    //update file list
        //    UpdateFileList();

        //}

        void ToList_Clicked(System.Object sender, System.EventArgs e)
        {
            //get name of file
            string filename = (string)((MenuItem)sender).BindingContext;
            List<string> jarjend = File.ReadAllLines(Path.Combine(folderPath, filename)).ToList();
            list.ItemsSource = jarjend;

        }

        void Delete_Clicked(System.Object sender, System.EventArgs e)
        {
            string filename = (string)((MenuItem)sender).BindingContext;
            File.Delete(Path.Combine(folderPath, filename));
            UpdateFileList();

        }
    }
}

