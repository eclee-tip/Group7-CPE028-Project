package com.example.pdapp

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.pdapp.databinding.FragmentLoginBinding


class LoginFragment : Fragment() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {

        val binding = DataBindingUtil.inflate<FragmentLoginBinding>(inflater, R.layout.fragment_login,container, false)

        binding.SignUp.setOnClickListener{view : View ->
            view.findNavController().navigate(R.id.action_loginFragment3_to_signupFragment)
        }

        binding.loginButton.setOnClickListener { view : View ->
            var uname = binding.username.text.toString()
            var pword = binding.password.text.toString()
            uname = '"' + uname + '"'
            pword = '"' + pword + '"'

            var db = DatabaseHandler(requireActivity())
            var data = db.readData(uname, pword)
            var result = data.size

            if(result > 0){
                view.findNavController().navigate(R.id.action_loginFragment3_to_homeFragment)
            }
            else{
                val toast = Toast.makeText(this.activity, "Invalid username or password", Toast.LENGTH_SHORT)
                toast.show()
            }
        }
        return binding.root
    }
}
