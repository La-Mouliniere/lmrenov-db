package scripts

import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.io.IOException

/**
 * A world-class Kotlin client for the FastAPI MongoDB Gateway.
 * 
 * Note: These methods use synchronous calls (.execute()). 
 * When integrating into your Android app, ensure these are called from a background 
 * thread or wrapped in a Coroutine (e.g., using withContext(Dispatchers.IO)).
 */
class Client(private val url: String, private val apiKey: String) {
    private val client = OkHttpClient()
    private val JSON_MEDIA_TYPE = "application/json; charset=utf-8".toMediaType()

    private val headers: Headers
        get() = Headers.Builder()
            .add("Authorization", "Bearer $apiKey")
            .add("Content-Type", "application/json")
            .build()

    /**
     * Returns the list of all collection names.
     */
    fun getCollections(): List<String> {
        val request = Request.Builder()
            .url("$url/collections")
            .headers(headers)
            .get()
            .build()

        client.newCall(request).execute().use { response ->
            if (!response.isSuccessful) throw IOException("Unexpected code $response")
            val bodyString = response.body?.string() ?: return emptyList()
            val json = JSONObject(bodyString)
            val collectionsArray = json.getJSONArray("collections")
            return List(collectionsArray.length()) { collectionsArray.getString(it) }
        }
    }

    /**
     * Creates a collection if it doesn't already exist.
     */
    fun createCollection(collectionName: String) {
        val collections = try { getCollections() } catch (e: Exception) { emptyList() }
        if (collections.contains(collectionName)) {
            println("The collection '$collectionName' already exists. Skip creation.")
            return
        }

        val request = Request.Builder()
            .url("$url/collections/$collectionName")
            .headers(headers)
            .post("{}".toRequestBody(JSON_MEDIA_TYPE))
            .build()

        client.newCall(request).execute().use { response ->
            if (!response.isSuccessful && response.code != 400) {
                throw IOException("Unexpected code $response")
            }
        }
    }

    fun createDocument(collectionName: String, jsonBody: String) {
        val request = Request.Builder()
            .url("$url/collections/$collectionName/documents")
            .headers(headers)
            .post(jsonBody.toRequestBody(JSON_MEDIA_TYPE))
            .build()

        client.newCall(request).execute().use { response ->
            if (!response.isSuccessful) throw IOException("Unexpected code $response")
        }
    }

    fun getDocuments(collectionName: String): String? {
        val request = Request.Builder()
            .url("$url/collections/$collectionName/documents")
            .headers(headers)
            .get()
            .build()

        client.newCall(request).execute().use { response ->
            if (!response.isSuccessful) throw IOException("Unexpected code $response")
            return response.body?.string()
        }
    }

    fun getDocument(collectionName: String, documentId: String): String? {
        val request = Request.Builder()
            .url("$url/collections/$collectionName/documents/$documentId")
            .headers(headers)
            .get()
            .build()

        client.newCall(request).execute().use { response ->
            if (!response.isSuccessful) throw IOException("Unexpected code $response")
            return response.body?.string()
        }
    }
}
