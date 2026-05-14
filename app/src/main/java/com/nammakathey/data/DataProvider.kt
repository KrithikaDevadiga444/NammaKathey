package com.nammakathey.data

import android.content.Context
import com.google.gson.Gson
import com.nammakathey.model.AppData
import com.nammakathey.model.District
import com.nammakathey.model.Hero
import java.io.InputStreamReader

object DataProvider {
    var appData: AppData? = null
    var isKannada: Boolean = false // Global toggle for language

    fun loadData(context: Context) {
        if (appData == null) {
            try {
                val inputStream = context.assets.open("data.json")
                val reader = InputStreamReader(inputStream)
                appData = Gson().fromJson(reader, AppData::class.java)
                reader.close()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    fun getDistricts(): List<District> {
        return appData?.districts ?: emptyList()
    }

    fun getDistrictById(id: String): District? {
        return appData?.districts?.find { it.id == id }
    }

    fun getHeroById(districtId: String, heroId: String): Hero? {
        return getDistrictById(districtId)?.heroes?.find { it.id == heroId }
    }
}
