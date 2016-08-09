package com.example.jatin.dialogdemo;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button=(Button)findViewById(R.id.click);
        button.setOnClickListener(this);

    }

    @Override
    public void onClick(View view) {
        MyDialog dialog=new MyDialog();
        dialog.show(getFragmentManager(),"123");
    }
}
