package com.vaadin.tutorial.crm;

import com.vaadin.flow.component.Text;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.datepicker.DatePicker;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.Route;


@Route("")
public class MainView extends VerticalLayout {

    public MainView() {

        //sample application in using verdin#

        //creating new elements
        Button button = new Button("I'm a button");
        DatePicker datePicker = new DatePicker("Pick a Date");

        //creating a new layout like qt
        HorizontalLayout layout = new HorizontalLayout(button,datePicker);
        layout.setDefaultVerticalComponentAlignment(Alignment.END);
        add(layout);


        //button listener to activiate an action
        button.addClickListener(clickEvent ->  add(new Text("Clicked: " + datePicker.getValue())));
    }

}
