package com.nammakathey.viewmodel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.nammakathey.data.DataProvider
import com.nammakathey.model.District

class MainViewModel(application: Application) : AndroidViewModel(application) {

    private val _districts = MutableLiveData<List<District>>()
    val districts: LiveData<List<District>> = _districts

    init {
        // Load data if not already loaded
        DataProvider.loadData(application)
        _districts.value = DataProvider.getDistricts()
    }
}
