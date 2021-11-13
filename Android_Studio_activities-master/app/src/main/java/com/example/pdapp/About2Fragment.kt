package com.example.pdapp

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.pdapp.databinding.FragmentAbout2Binding


class About2Fragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?): View? {
        val binding = DataBindingUtil.inflate<FragmentAbout2Binding>(inflater,
            R.layout.fragment_about2,container,false)

        binding.aback.setOnClickListener{ view : View ->
            view.findNavController().navigate(R.id.action_AAboutFragment_to_homeFragment)
        }
        return binding.root
    }
}